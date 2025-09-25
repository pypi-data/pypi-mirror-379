"""
Batch models for the Rose Python SDK.
"""

from typing import Dict, Any
from .base import BaseModel
from pydantic import Field


class BatchIDInfo(BaseModel):
    """Batch ID info model."""

    updated_at: int
    index: str


class ImportFileInfo(BaseModel):
    """Import file information model."""

    header: Dict[str, Any]
    url: str


class BatchRecordsImportInfo(BaseModel):
    """Batch records import info model."""

    import_: Dict[str, ImportFileInfo] = Field(alias="import")
