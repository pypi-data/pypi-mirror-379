"""Pydantic models for the Selection configuration."""

from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel


class SelectionConfig(BaseModel):
    """Configuration for the selection process."""

    dataset_id: UUID
    n_samples_to_select: int
    selection_result_tag_name: str
    strategies: list[SelectionStrategy]


class SelectionStrategy(BaseModel):
    """Base class for selection strategies."""

    strength: float = 1.0


class EmbeddingDiversityStrategy(SelectionStrategy):
    """Selection strategy based on embedding diversity."""

    embedding_model_name: str | None


class MetadataWeightingStrategy(SelectionStrategy):
    """Selection strategy based on metadata weighting."""

    metadata_key: str
