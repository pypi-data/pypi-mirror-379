"""
Data models for the Entangle Matrix SDK.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from datetime import datetime


@dataclass
class MatrixMessage:
    """Represents a Matrix message response."""

    event_id: str
    room_id: str
    timestamp: str
    message: str
    metadata: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MatrixMessage":
        """Create MatrixMessage from API response data."""
        return cls(
            event_id=data["event_id"],
            room_id=data["room_id"],
            timestamp=data["timestamp"],
            message=data["message"],
            metadata=data.get("metadata", {}),
        )


@dataclass
class MatrixUpload:
    """Represents a Matrix media upload response."""

    event_id: str
    room_id: str
    mxc_uri: str
    file_name: str
    file_size: int
    content_type: str
    metadata: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MatrixUpload":
        """Create MatrixUpload from API response data."""
        return cls(
            event_id=data["event_id"],
            room_id=data["room_id"],
            mxc_uri=data["mxc_uri"],
            file_name=data["file_name"],
            file_size=data["file_size"],
            content_type=data["content_type"],
            metadata=data.get("metadata", {}),
        )


@dataclass
class MatrixRoom:
    """Represents a Matrix room."""

    room_id: str
    name: Optional[str]
    topic: Optional[str]
    avatar_url: Optional[str]
    member_count: int
    is_encrypted: bool
    is_direct: bool
    metadata: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MatrixRoom":
        """Create MatrixRoom from API response data."""
        return cls(
            room_id=data["room_id"],
            name=data.get("name"),
            topic=data.get("topic"),
            avatar_url=data.get("avatar_url"),
            member_count=data["member_count"],
            is_encrypted=data["is_encrypted"],
            is_direct=data["is_direct"],
            metadata=data.get("metadata", {}),
        )


@dataclass
class MessageRequest:
    """Request data for sending a message."""

    room_id: str
    message: str
    formatted_body: Optional[str] = None
    format_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API request."""
        data = {
            "room_id": self.room_id,
            "message": self.message,
        }
        if self.formatted_body:
            data["formatted_body"] = self.formatted_body
        if self.format_type:
            data["format_type"] = self.format_type
        return data


@dataclass
class CreateRoomRequest:
    """Request data for creating a room."""

    name: str
    topic: Optional[str] = None
    is_public: bool = False
    is_direct: bool = False
    invite_users: Optional[List[str]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API request."""
        data = {
            "name": self.name,
            "is_public": self.is_public,
            "is_direct": self.is_direct,
        }
        if self.topic:
            data["topic"] = self.topic
        if self.invite_users:
            data["invite_users"] = self.invite_users
        return data


@dataclass
class JoinRoomRequest:
    """Request data for joining a room."""

    room_id_or_alias: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API request."""
        return {"room_id_or_alias": self.room_id_or_alias}


@dataclass
class APIResponse:
    """Standard API response wrapper."""

    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "APIResponse":
        """Create APIResponse from response data."""
        return cls(
            success=data.get("success", False),
            message=data.get("message", ""),
            data=data.get("data"),
            error=data.get("error"),
        )