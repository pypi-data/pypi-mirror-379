"""API endpoints for annotation tasks."""

from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from lightly_studio.db_manager import SessionDep
from lightly_studio.models.annotation_task import AnnotationTaskTable
from lightly_studio.resolvers import annotation_task_resolver

router = APIRouter(prefix="/annotationtasks", tags=["annotationtasks"])


@router.get("/", response_model=List[AnnotationTaskTable])
def get_annotation_tasks(
    session: SessionDep,
) -> List[AnnotationTaskTable]:
    """Get all annotation tasks."""
    return annotation_task_resolver.get_all(session=session)


@router.get("/{annotation_task_id}", response_model=AnnotationTaskTable)
def get_annotation_task(
    annotation_task_id: UUID,
    session: SessionDep,
) -> AnnotationTaskTable:
    """Get an annotation task by ID."""
    task = annotation_task_resolver.get_by_id(
        session=session, annotation_task_id=annotation_task_id
    )
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Annotation task with ID {annotation_task_id} not found",
        )
    return task
