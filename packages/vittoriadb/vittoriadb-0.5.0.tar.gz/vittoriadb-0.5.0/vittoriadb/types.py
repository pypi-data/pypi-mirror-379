"""
Data types and structures for VittoriaDB Python client.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum


class DistanceMetric(Enum):
    """Distance metrics for vector similarity calculation."""
    COSINE = 0
    EUCLIDEAN = 1
    DOT_PRODUCT = 2
    MANHATTAN = 3
    
    @classmethod
    def from_string(cls, value: str) -> 'DistanceMetric':
        """Create DistanceMetric from string value."""
        string_map = {
            "cosine": cls.COSINE,
            "euclidean": cls.EUCLIDEAN,
            "dot_product": cls.DOT_PRODUCT,
            "manhattan": cls.MANHATTAN
        }
        return string_map.get(value.lower(), cls.COSINE)
    
    def to_string(self) -> str:
        """Convert to string representation."""
        string_map = {
            self.COSINE: "cosine",
            self.EUCLIDEAN: "euclidean", 
            self.DOT_PRODUCT: "dot_product",
            self.MANHATTAN: "manhattan"
        }
        return string_map.get(self, "cosine")


class IndexType(Enum):
    """Vector index types."""
    FLAT = 0
    HNSW = 1
    IVF = 2
    
    @classmethod
    def from_string(cls, value: str) -> 'IndexType':
        """Create IndexType from string value."""
        string_map = {
            "flat": cls.FLAT,
            "hnsw": cls.HNSW,
            "ivf": cls.IVF
        }
        return string_map.get(value.lower(), cls.FLAT)
    
    def to_string(self) -> str:
        """Convert to string representation."""
        string_map = {
            self.FLAT: "flat",
            self.HNSW: "hnsw",
            self.IVF: "ivf"
        }
        return string_map.get(self, "flat")


class VectorizerType(Enum):
    """Vectorizer types for automatic embedding generation."""
    NONE = 0
    SENTENCE_TRANSFORMERS = 1
    OPENAI = 2
    HUGGINGFACE = 3
    OLLAMA = 4
    
    @classmethod
    def from_string(cls, value: str) -> 'VectorizerType':
        """Create VectorizerType from string value."""
        string_map = {
            "none": cls.NONE,
            "sentence_transformers": cls.SENTENCE_TRANSFORMERS,
            "openai": cls.OPENAI,
            "huggingface": cls.HUGGINGFACE,
            "ollama": cls.OLLAMA
        }
        return string_map.get(value.lower(), cls.NONE)
    
    def to_string(self) -> str:
        """Convert to string representation."""
        string_map = {
            self.NONE: "none",
            self.SENTENCE_TRANSFORMERS: "sentence_transformers",
            self.OPENAI: "openai",
            self.HUGGINGFACE: "huggingface",
            self.OLLAMA: "ollama"
        }
        return string_map.get(self, "none")


@dataclass
class VectorizerConfig:
    """Configuration for automatic vectorization."""
    type: VectorizerType
    model: str
    dimensions: int
    options: Dict[str, Any]
    
    def __post_init__(self):
        if self.options is None:
            self.options = {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API calls."""
        return {
            "type": self.type.value,  # Send integer value, not string
            "model": self.model,
            "dimensions": self.dimensions,
            "options": self.options
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'VectorizerConfig':
        """Create VectorizerConfig from dictionary."""
        return cls(
            type=VectorizerType.from_string(data["type"]),
            model=data["model"],
            dimensions=data["dimensions"],
            options=data.get("options", {})
        )


@dataclass
class Vector:
    """Represents a vector with metadata."""
    id: str
    vector: List[float]
    metadata: Optional[Dict[str, Any]] = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class ContentStorageConfig:
    """Configuration for content storage."""
    enabled: bool = True
    field_name: str = "_content"
    max_size: int = 1048576  # 1MB default
    compressed: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API calls."""
        return {
            "enabled": self.enabled,
            "field_name": self.field_name,
            "max_size": self.max_size,
            "compressed": self.compressed
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ContentStorageConfig':
        """Create ContentStorageConfig from dictionary."""
        return cls(
            enabled=data.get("enabled", True),
            field_name=data.get("field_name", "_content"),
            max_size=data.get("max_size", 1048576),
            compressed=data.get("compressed", False)
        )


@dataclass
class SearchResult:
    """Represents a search result."""
    id: str
    score: float
    vector: Optional[List[float]] = None
    metadata: Optional[Dict[str, Any]] = None
    content: Optional[str] = None  # NEW: Original content if available

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SearchResult':
        """Create SearchResult from dictionary."""
        return cls(
            id=data["id"],
            score=data["score"],
            vector=data.get("vector"),
            metadata=data.get("metadata"),
            content=data.get("content")  # NEW: Include content field
        )
    
    def has_content(self) -> bool:
        """Check if this result has original content."""
        return self.content is not None and self.content != ""
    
    def get_content(self, content_field_name: str = "_content") -> str:
        """Get original content from content field or metadata."""
        if self.content:
            return self.content
        
        if self.metadata and content_field_name in self.metadata:
            return str(self.metadata[content_field_name])
        
        return ""


@dataclass
class CollectionInfo:
    """Represents collection information."""
    name: str
    dimensions: int
    metric: DistanceMetric
    index_type: IndexType
    vector_count: int
    created: str
    modified: str
    content_storage: Optional[ContentStorageConfig] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CollectionInfo':
        """Create CollectionInfo from dictionary."""
        content_storage = None
        if "content_storage" in data and data["content_storage"]:
            content_storage = ContentStorageConfig.from_dict(data["content_storage"])
        
        return cls(
            name=data["name"],
            dimensions=data["dimensions"],
            metric=DistanceMetric(data["metric"]),
            index_type=IndexType(data["index_type"]),
            vector_count=data["vector_count"],
            created=data["created"],
            modified=data["modified"],
            content_storage=content_storage
        )


@dataclass
class HealthStatus:
    """Represents database health status."""
    status: str
    uptime: int
    collections: int
    total_vectors: int
    memory_usage: int
    disk_usage: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'HealthStatus':
        """Create HealthStatus from dictionary."""
        return cls(
            status=data["status"],
            uptime=data["uptime"],
            collections=data["collections"],
            total_vectors=data["total_vectors"],
            memory_usage=data["memory_usage"],
            disk_usage=data["disk_usage"]
        )


@dataclass
class DatabaseStats:
    """Represents database statistics."""
    total_vectors: int
    total_size: int
    index_size: int
    queries_total: int
    queries_per_sec: float
    avg_query_latency: float
    collections: List[Dict[str, Any]]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DatabaseStats':
        """Create DatabaseStats from dictionary."""
        return cls(
            total_vectors=data["total_vectors"],
            total_size=data["total_size"],
            index_size=data["index_size"],
            queries_total=data["queries_total"],
            queries_per_sec=data["queries_per_sec"],
            avg_query_latency=data["avg_query_latency"],
            collections=data["collections"]
        )


class VittoriaDBError(Exception):
    """Base exception for VittoriaDB errors."""
    pass


class ConnectionError(VittoriaDBError):
    """Raised when connection to VittoriaDB fails."""
    pass


class CollectionError(VittoriaDBError):
    """Raised when collection operations fail."""
    pass


class VectorError(VittoriaDBError):
    """Raised when vector operations fail."""
    pass


class SearchError(VittoriaDBError):
    """Raised when search operations fail."""
    pass


class BinaryError(VittoriaDBError):
    """Raised when binary management fails."""
    pass


@dataclass
class UnifiedConfig:
    """Unified configuration for VittoriaDB v0.5.0+."""
    server: Optional[Dict[str, Any]] = None
    storage: Optional[Dict[str, Any]] = None
    search: Optional[Dict[str, Any]] = None
    embeddings: Optional[Dict[str, Any]] = None
    performance: Optional[Dict[str, Any]] = None
    log: Optional[Dict[str, Any]] = None
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UnifiedConfig':
        """Create UnifiedConfig from dictionary."""
        return cls(
            server=data.get("server"),
            storage=data.get("storage"),
            search=data.get("search"),
            embeddings=data.get("embeddings"),
            performance=data.get("performance"),
            log=data.get("log")
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        result = {}
        if self.server is not None:
            result["server"] = self.server
        if self.storage is not None:
            result["storage"] = self.storage
        if self.search is not None:
            result["search"] = self.search
        if self.embeddings is not None:
            result["embeddings"] = self.embeddings
        if self.performance is not None:
            result["performance"] = self.performance
        if self.log is not None:
            result["log"] = self.log
        return result


@dataclass
class ConfigurationInfo:
    """Information about VittoriaDB configuration (v0.5.0+)."""
    config: UnifiedConfig
    metadata: Dict[str, Any]
    feature_flags: Dict[str, bool]
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ConfigurationInfo':
        """Create ConfigurationInfo from dictionary."""
        return cls(
            config=UnifiedConfig.from_dict(data.get("config", {})),
            metadata=data.get("metadata", {}),
            feature_flags=data.get("feature_flags", {})
        )
