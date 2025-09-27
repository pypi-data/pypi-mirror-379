"""
Base schema models for Strala applications.
"""

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel as PydanticBaseModel, Field, ConfigDict


class BaseModel(PydanticBaseModel):
    """
    Base model class with common configuration and fields.
    """
    
    model_config = ConfigDict(
        # Allow extra fields for flexibility
        extra="allow",
        # Use enum values instead of enum objects
        use_enum_values=True,
        # Validate assignment
        validate_assignment=True,
        # Populate by name (allows field aliases)
        populate_by_name=True,
    )
    
    created_at: Optional[datetime] = Field(
        default=None,
        description="Timestamp when the record was created"
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        description="Timestamp when the record was last updated"
    )
    
    def dict_exclude_none(self) -> Dict[str, Any]:
        """Return dictionary representation excluding None values."""
        return self.model_dump(exclude_none=True)
    
    def dict_exclude_unset(self) -> Dict[str, Any]:
        """Return dictionary representation excluding unset values."""
        return self.model_dump(exclude_unset=True)
