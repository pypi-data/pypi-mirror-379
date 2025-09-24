"""
File Manager

This module provides the YAPFileManager class, which is the main class for managing files.
It combines all the mixins to provide a unified API for all file formats.
"""

from pathlib import Path
from typing import (
    Any,
    Dict,
    ItemsView,
    Iterator,
    KeysView,
    List,
    Optional,
    Union,
    ValuesView,
)

from yapfm.cache import LazySectionLoader, SmartCache
from yapfm.strategies import BaseFileStrategy

from .exceptions import StrategyError
from .helpers import validate_strategy
from .mixins import (
    AnalysisMixin,
    CacheMixin,
    CleanupMixin,
    CloneMixin,
    ContextMixin,
    ExportMixin,
    FileOperationsMixin,
    KeyOperationsMixin,
    LazySectionsMixin,
    MultiFileMixin,
    SearchMixin,
    SectionOperationsMixin,
    SecurityMixin,
    StreamingMixin,
    TransformMixin,
)
from .registry import FileStrategyRegistry


class YAPFileManager(
    FileOperationsMixin,
    ContextMixin,
    KeyOperationsMixin,
    SectionOperationsMixin,
    CacheMixin,
    LazySectionsMixin,
    MultiFileMixin,
    StreamingMixin,
    SearchMixin,
    CloneMixin,
    AnalysisMixin,
    TransformMixin,
    CleanupMixin,
    SecurityMixin,
    ExportMixin,
):
    unified_cache: Optional[SmartCache]

    def __init__(
        self,
        path: Union[str, Path],
        strategy: Optional[BaseFileStrategy] = None,
        *,
        auto_create: bool = False,
        enable_context: bool = True,
        enable_cache: bool = True,
        cache_size: int = 1000,  # default 1000 keys
        cache_ttl: Optional[float] = 3600,  # 1 hour
        enable_streaming: bool = False,
        enable_lazy_loading: bool = False,
        **kwargs: Any,
    ) -> None:
        """
        Initialize the FileManager with mixins.
        """
        # Set up path and strategy
        self.path = Path(path)

        if strategy is None:
            strategy = FileStrategyRegistry.get_strategy(self.path.suffix.lower())
            if strategy is None:
                raise StrategyError(
                    f"No strategy found for extension: {self.path.suffix}"
                )

        self.strategy = strategy
        validate_strategy(strategy)
        self.auto_create = auto_create
        self.document: Dict[str, Any] = {}

        # Store cache configuration
        self.enable_cache = enable_cache
        self.cache_size = cache_size
        self.cache_ttl = cache_ttl
        self.enable_lazy_loading = enable_lazy_loading

        # Initialize unified cache system
        self._init_unified_cache()

        super().__init__(**kwargs)

    def _init_unified_cache(self) -> None:
        """Initialize the unified cache system."""
        # Unified cache for all operations
        if self.enable_cache:
            self.unified_cache = SmartCache(
                max_size=self.cache_size, default_ttl=self.cache_ttl, track_stats=True
            )
        else:
            self.unified_cache = None

        # Lazy loaders for sections only
        self._lazy_sections: Dict[str, LazySectionLoader] = {}

        # Cache for generated keys (performance optimization)
        self._key_cache: Dict[str, str] = {}

    def get_cache(self) -> Optional[SmartCache]:
        """Get the unified cache."""
        if self.enable_cache:
            return self.unified_cache
        return None

    def clear_key_cache(self) -> None:
        """
        Clear the key generation cache.

        This method clears the internal cache used for key generation,
        which can be useful for memory management or when you want to
        force regeneration of cache keys.

        Example:
            >>> fm = YAPFileManager("config.json")
            >>> fm.get_key("database.host")  # Generates and caches key
            >>> fm.clear_key_cache()  # Clears the key cache
        """
        self._key_cache.clear()

    def get_cache_stats(self) -> Dict[str, Any]:
        """
        Get comprehensive cache statistics.

        Returns:
            Dictionary containing cache statistics including:
            - unified_cache: Statistics from the main cache
            - lazy_sections: Statistics from lazy loading
            - key_cache: Statistics from key generation cache

        Example:
            >>> stats = fm.get_cache_stats()
            >>> print(f"Cache hits: {stats['unified_cache']['hits']}")
            >>> print(f"Lazy sections: {stats['lazy_sections']['total_sections']}")
        """
        stats = {
            "unified_cache": {},
            "lazy_sections": {},
            "key_cache": {"size": len(self._key_cache)},
        }

        # Unified cache stats
        if self.unified_cache:
            stats["unified_cache"] = self.unified_cache.get_stats()

        # Lazy sections stats
        if hasattr(self, "get_lazy_stats"):
            stats["lazy_sections"] = self.get_lazy_stats()

        return stats

    def _generate_cache_key(
        self,
        dot_key: Optional[str],
        path: Optional[List[str]],
        key_name: Optional[str],
        key_type: str = "key",
    ) -> str:
        """Generate a cache key from the key parameters with caching."""
        # Create a unique key for caching
        if dot_key is not None:
            cache_input = f"{key_type}:{dot_key}"
        elif path is not None and key_name is not None:
            path_str = ".".join(path) if path else ""
            cache_input = (
                f"{key_type}:{path_str}.{key_name}"
                if path_str
                else f"{key_type}:{key_name}"
            )
        else:
            raise ValueError("Cannot generate cache key without key parameters")

        # Check cache first
        if cache_input in self._key_cache:
            return self._key_cache[cache_input]

        # Generate and cache the key
        self._key_cache[cache_input] = cache_input
        return cache_input

    @property
    def data(self) -> Dict[str, Any]:
        """
        Get the file data, loading it if necessary.

        Returns:
            Dictionary containing the file data

        Note:
            This property automatically loads the file on first access
            if it hasn't been loaded yet.
        """
        self.load_if_not_loaded()
        return self.document

    @data.setter
    def data(self, value: Dict[str, Any]) -> None:
        """
        Set the file data.

        Args:
            value: Dictionary containing the data to set

        Raises:
            TypeError: If value is not a dictionary
        """
        if not isinstance(value, dict):
            raise TypeError("Data must be a dictionary")
        self.document = value
        self.mark_as_loaded()
        self.mark_as_dirty()

    # -----------------------
    # Simplified API methods (delegating to mixins)
    # -----------------------

    def set(
        self,
        key: str,
        value: Any,
        overwrite: bool = True,
    ) -> None:
        """Set a value in the file using key."""
        self.check_frozen()
        return self.set_value(key, value, overwrite=overwrite)

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """Get a value from the file using key with caching."""
        return self.get_value(key, default=default)

    def has(self, key: str) -> bool:
        """Check if a key exists in the file."""
        return self.has_key(dot_key=key)

    def delete(self, key: str) -> bool:
        """Delete a key from the file."""
        self.check_frozen()
        return self.delete_key(dot_key=key)

    # -----------------------
    # Dict-like API
    # -----------------------

    def __getitem__(self, key: str) -> Any:
        """Get item using dict-like syntax."""
        return self.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        """Set item using dict-like syntax."""
        self.check_frozen()
        self.set(key, value)

    def __contains__(self, key: str) -> bool:
        """Check if key exists using dict-like syntax."""
        return self.has(key)

    def __delitem__(self, key: str) -> None:
        """Delete item using dict-like syntax."""
        self.check_frozen()
        self.delete(key)

    def __len__(self) -> int:
        """Get number of top-level keys."""
        return len(self.data)

    def __iter__(self) -> Iterator[str]:
        """Iterate over top-level keys."""
        return iter(self.data)

    def keys(self) -> KeysView[str]:
        """Get all top-level keys."""
        return self.data.keys()

    def values(self) -> ValuesView[Any]:
        """Get all top-level values."""
        return self.data.values()

    def items(self) -> ItemsView[str, Any]:
        """Get all top-level key-value pairs."""
        return self.data.items()

    def pop(self, key: str, default: Any = None) -> Any:
        """Pop value and remove key."""
        self.check_frozen()
        if self.has(key):
            value = self.get(key)
            self.delete(key)
            return value
        else:
            return default

    def update(self, other: Dict[str, Any]) -> None:
        """Update with another dictionary."""
        self.check_frozen()
        for key, value in other.items():
            self.set(key, value)

    def clear(self) -> None:
        """Clear all data."""
        self.check_frozen()
        self.data.clear()
        self.mark_as_dirty()

    # -----------------------
    # Batch operations
    # -----------------------
    def set_multiple(self, items: Dict[str, Any], overwrite: bool = True) -> None:
        """
        Set multiple key-value pairs efficiently.

        Args:
            items: Dictionary of key-value pairs to set.
            overwrite: Whether to overwrite existing values.

        Example:
            >>> fm.set_multiple({
            ...     "database.host": "localhost",
            ...     "database.port": 5432,
            ...     "logging.level": "INFO"
            ... })

        Raises:
            ValueError: If any key fails to be set.
        """
        self.check_frozen()
        if not items:
            return

        # Track failed operations for better error reporting
        failed_keys = []
        for key, value in items.items():
            try:
                self.set(key, value, overwrite)
            except Exception as e:
                failed_keys.append((key, str(e)))

        if failed_keys:
            raise ValueError(f"Failed to set keys: {failed_keys}")

    def get_multiple(
        self,
        keys: List[str],
        default: Any = None,
        defaults: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Get multiple values efficiently.

        Args:
            keys: List of keys to get.
            default: Default value for missing keys.
            defaults: Optional dictionary with specific default values per key.

        Returns:
            Dictionary with key-value pairs.

        Example:
            >>> values = fm.get_multiple(["database.host", "database.port"])
            >>> values = fm.get_multiple(
            ...     ["database.host", "database.port"],
            ...     defaults={"database.host": "localhost", "database.port": 5432}
            ... )
        """
        if not keys:
            return {}

        result = {}
        for key in keys:
            key_default = defaults.get(key, default) if defaults else default
            result[key] = self.get(key, key_default)
        return result

    def delete_multiple(self, keys: List[str]) -> int:
        """
        Delete multiple keys efficiently.

        Args:
            keys: List of keys to delete.

        Returns:
            Number of keys deleted.

        Example:
            >>> deleted_count = fm.delete_multiple(["database.host", "database.port"])

        Raises:
            ValueError: If keys is not a list or contains invalid keys.
        """
        self.check_frozen()
        if not isinstance(keys, list):
            raise ValueError("Keys must be a list")

        if not keys:
            return 0

        deleted = 0
        for key in keys:
            if not isinstance(key, str):
                raise ValueError(f"All keys must be strings, got: {type(key)}")
            if self.delete(key):
                deleted += 1
        return deleted

    def has_multiple(self, keys: List[str]) -> Dict[str, bool]:
        """
        Check existence of multiple keys efficiently.

        Args:
            keys: List of keys to check.

        Returns:
            Dictionary with key-existence pairs.

        Example:
            >>> exists = fm.has_multiple(["database.host", "database.port"])

        Raises:
            ValueError: If keys is not a list or contains invalid keys.
        """
        if not isinstance(keys, list):
            raise ValueError("Keys must be a list")

        if not keys:
            return {}

        result = {}
        for key in keys:
            if not isinstance(key, str):
                raise ValueError(f"All keys must be strings, got: {type(key)}")
            result[key] = self.has(key)
        return result
