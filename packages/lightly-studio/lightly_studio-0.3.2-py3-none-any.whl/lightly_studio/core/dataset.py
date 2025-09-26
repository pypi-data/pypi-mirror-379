"""LightlyStudio Dataset."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Iterator
from uuid import UUID

from labelformat.formats import (
    COCOInstanceSegmentationInput,
    COCOObjectDetectionInput,
    YOLOv8ObjectDetectionInput,
)
from labelformat.model.instance_segmentation import (
    InstanceSegmentationInput,
)
from labelformat.model.object_detection import (
    ObjectDetectionInput,
)
from sqlmodel import Session, select

from lightly_studio import db_manager
from lightly_studio.api import features
from lightly_studio.core import add_samples
from lightly_studio.core.dataset_query.dataset_query import DatasetQuery
from lightly_studio.core.dataset_query.match_expression import MatchExpression
from lightly_studio.core.dataset_query.order_by import OrderByExpression
from lightly_studio.core.sample import Sample
from lightly_studio.dataset import fsspec_lister
from lightly_studio.dataset.embedding_manager import EmbeddingManagerProvider
from lightly_studio.models.annotation_task import (
    AnnotationTaskTable,
    AnnotationType,
)
from lightly_studio.models.dataset import DatasetCreate, DatasetTable
from lightly_studio.models.sample import SampleTable
from lightly_studio.resolvers import (
    annotation_task_resolver,
    dataset_resolver,
    sample_resolver,
)
from lightly_studio.type_definitions import PathLike

# Constants
DEFAULT_DATASET_NAME = "default_dataset"

_SliceType = slice  # to avoid shadowing built-in slice in type annotations


class Dataset:
    """A LightlyStudio Dataset.

    Keeps a reference to the underlying DatasetTable.
    """

    def __init__(self, dataset: DatasetTable) -> None:
        """Initialize a LightlyStudio Dataset."""
        self._inner = dataset
        # TODO(Michal, 09/2025): Do not store the session. Instead, use the
        # dataset object session.
        self.session = db_manager.persistent_session()

    @staticmethod
    def create(name: str | None = None) -> Dataset:
        """Create a new dataset."""
        if name is None:
            name = DEFAULT_DATASET_NAME

        dataset = dataset_resolver.create(
            session=db_manager.persistent_session(),
            dataset=DatasetCreate(name=name, directory=""),
        )
        return Dataset(dataset=dataset)

    @staticmethod
    def load(name: str | None = None) -> Dataset:
        """Load an existing dataset."""
        if name is None:
            name = "default_dataset"

        dataset = dataset_resolver.get_by_name(session=db_manager.persistent_session(), name=name)
        if dataset is None:
            raise ValueError(f"Dataset with name '{name}' not found.")

        return Dataset(dataset=dataset)

    @staticmethod
    def load_or_create(name: str | None = None) -> Dataset:
        """Create a new dataset or load an existing one."""
        if name is None:
            name = "default_dataset"

        dataset = dataset_resolver.get_by_name(session=db_manager.persistent_session(), name=name)
        if dataset is None:
            return Dataset.create(name=name)

        return Dataset(dataset=dataset)

    def __iter__(self) -> Iterator[Sample]:
        """Iterate over samples in the dataset."""
        for sample in self.session.exec(
            select(SampleTable).where(SampleTable.dataset_id == self.dataset_id)
        ):
            yield Sample(inner=sample)

    def get_sample(self, sample_id: UUID) -> Sample:
        """Get a single sample from the dataset by its ID.

        Args:
            sample_id: The UUID of the sample to retrieve.

        Returns:
            A single SampleTable object.

        Raises:
            IndexError: If no sample is found with the given sample_id.
        """
        sample = sample_resolver.get_by_id(
            self.session, dataset_id=self.dataset_id, sample_id=sample_id
        )

        if sample is None:
            raise IndexError(f"No sample found for sample_id: {sample_id}")
        return Sample(inner=sample)

    @property
    def dataset_id(self) -> UUID:
        """Get the dataset ID."""
        return self._inner.dataset_id

    @property
    def name(self) -> str:
        """Get the dataset name."""
        return self._inner.name

    def query(self) -> DatasetQuery:
        """Create a DatasetQuery for this dataset.

        Returns:
            A DatasetQuery instance for querying samples in this dataset.
        """
        return DatasetQuery(dataset=self._inner, session=self.session)

    def match(self, match_expression: MatchExpression) -> DatasetQuery:
        """Create a query on the dataset and store a field condition for filtering.

        Args:
            match_expression: Defines the filter.

        Returns:
            DatasetQuery for method chaining.
        """
        return self.query().match(match_expression)

    def order_by(self, *order_by: OrderByExpression) -> DatasetQuery:
        """Create a query on the dataset and store ordering expressions.

        Args:
            order_by: One or more ordering expressions. They are applied in order.
                E.g. first ordering by sample width and then by sample file_name will
                only order the samples with the same sample width by file_name.

        Returns:
            DatasetQuery for method chaining.
        """
        return self.query().order_by(*order_by)

    def slice(self, offset: int = 0, limit: int | None = None) -> DatasetQuery:
        """Create a query on the dataset and apply offset and limit to results.

        Args:
            offset: Number of items to skip from beginning (default: 0).
            limit: Maximum number of items to return (None = no limit).

        Returns:
            DatasetQuery for method chaining.
        """
        return self.query().slice(offset, limit)

    def __getitem__(self, key: _SliceType) -> DatasetQuery:
        """Create a query on the dataset and enable bracket notation for slicing.

        Args:
            key: A slice object (e.g., [10:20], [:50], [100:]).

        Returns:
            DatasetQuery with slice applied.

        Raises:
            TypeError: If key is not a slice object.
            ValueError: If slice contains unsupported features or conflicts with existing slice.
        """
        return self.query()[key]

    def add_samples_from_path(
        self,
        path: PathLike,
        allowed_extensions: Iterable[str] | None = None,
        embed: bool = True,
    ) -> None:
        """Adding samples from the specified path to the dataset.

        Args:
            path: Path to the folder containing the images to add.
            allowed_extensions: An iterable container of allowed image file
                extensions.
            embed: If True, generate embeddings for the newly added samples.
        """
        # Collect image file paths.
        if allowed_extensions:
            allowed_extensions_set = {ext.lower() for ext in allowed_extensions}
        else:
            allowed_extensions_set = None
        image_paths = list(
            fsspec_lister.iter_files_from_path(
                path=str(path), allowed_extensions=allowed_extensions_set
            )
        )
        print(f"Found {len(image_paths)} images in {path}.")

        # Process images.
        created_sample_ids = add_samples.load_into_dataset_from_paths(
            session=self.session,
            dataset_id=self.dataset_id,
            image_paths=image_paths,
        )

        if embed:
            _generate_embeddings(
                session=self.session, dataset_id=self.dataset_id, sample_ids=created_sample_ids
            )

    def add_samples_from_labelformat(
        self,
        input_labels: ObjectDetectionInput | InstanceSegmentationInput,
        images_path: PathLike,
        is_prediction: bool = True,
        task_name: str | None = None,
        embed: bool = True,
    ) -> None:
        """Load a dataset from a labelformat object and store in database.

        Args:
            input_labels: The labelformat input object.
            images_path: Path to the folder containing the images.
            is_prediction: Whether the task is for prediction or labels.
            task_name: Optional name for the annotation task. If None, a
                default name is generated.
            embed: If True, generate embeddings for the newly added samples.
        """
        if isinstance(images_path, str):
            images_path = Path(images_path)
        images_path = images_path.absolute()

        # Determine annotation type based on input.
        # Currently, we always create BBOX tasks, even for segmentation,
        # as segmentation data is stored alongside bounding boxes.
        annotation_type = AnnotationType.BBOX

        # Generate a default task name if none is provided.
        if task_name is None:
            task_name = f"Loaded from labelformat: {self.name}"

        # Create annotation task.
        new_annotation_task = annotation_task_resolver.create(
            session=self.session,
            annotation_task=AnnotationTaskTable(
                name=task_name,
                annotation_type=annotation_type,
                is_prediction=is_prediction,
            ),
        )

        created_sample_ids = add_samples.load_into_dataset_from_labelformat(
            session=self.session,
            dataset_id=self.dataset_id,
            input_labels=input_labels,
            images_path=images_path,
            annotation_task_id=new_annotation_task.annotation_task_id,
        )

        if embed:
            _generate_embeddings(
                session=self.session, dataset_id=self.dataset_id, sample_ids=created_sample_ids
            )

    def add_samples_from_yolo(
        self,
        data_yaml: PathLike,
        input_split: str = "train",
        task_name: str | None = None,
        embed: bool = True,
    ) -> None:
        """Load a dataset in YOLO format and store in DB.

        Args:
            data_yaml: Path to the YOLO data.yaml file.
            input_split: The split to load (e.g., 'train', 'val').
            task_name: Optional name for the annotation task. If None, a
                default name is generated.
            embed: If True, generate embeddings for the newly added samples.
        """
        if isinstance(data_yaml, str):
            data_yaml = Path(data_yaml)
        data_yaml = data_yaml.absolute()

        if not data_yaml.is_file() or data_yaml.suffix != ".yaml":
            raise FileNotFoundError(f"YOLO data yaml file not found: '{data_yaml}'")

        if task_name is None:
            task_name = f"Loaded from YOLO: {data_yaml.name} ({input_split} split)"

        # Load the dataset using labelformat.
        label_input = YOLOv8ObjectDetectionInput(
            input_file=data_yaml,
            input_split=input_split,
        )
        images_path = label_input._images_dir()  # noqa: SLF001

        self.add_samples_from_labelformat(
            input_labels=label_input,
            images_path=images_path,
            is_prediction=False,
            task_name=task_name,
            embed=embed,
        )

    def add_samples_from_coco(
        self,
        annotations_json: PathLike,
        images_path: PathLike,
        task_name: str | None = None,
        annotation_type: AnnotationType = AnnotationType.BBOX,
        embed: bool = True,
    ) -> None:
        """Load a dataset in COCO Object Detection format and store in DB.

        Args:
            annotations_json: Path to the COCO annotations JSON file.
            images_path: Path to the folder containing the images.
            task_name: Optional name for the annotation task. If None, a
                default name is generated.
            annotation_type: The type of annotation to be loaded (e.g., 'ObjectDetection',
                'InstanceSegmentation').
            embed: If True, generate embeddings for the newly added samples.
        """
        if isinstance(annotations_json, str):
            annotations_json = Path(annotations_json)
        annotations_json = annotations_json.absolute()

        if not annotations_json.is_file() or annotations_json.suffix != ".json":
            raise FileNotFoundError(f"COCO annotations json file not found: '{annotations_json}'")

        label_input: COCOObjectDetectionInput | COCOInstanceSegmentationInput

        if annotation_type == AnnotationType.BBOX:
            label_input = COCOObjectDetectionInput(
                input_file=annotations_json,
            )
            task_name_default = f"Loaded from COCO Object Detection: {annotations_json.name}"
        elif annotation_type == AnnotationType.INSTANCE_SEGMENTATION:
            label_input = COCOInstanceSegmentationInput(
                input_file=annotations_json,
            )
            task_name_default = f"Loaded from COCO Instance Segmentation: {annotations_json.name}"
        else:
            raise ValueError(f"Invalid annotation type: {annotation_type}")

        if task_name is None:
            task_name = task_name_default

        images_path = Path(images_path).absolute()

        self.add_samples_from_labelformat(
            input_labels=label_input,
            images_path=images_path,
            is_prediction=False,
            task_name=task_name,
            embed=embed,
        )


def _generate_embeddings(session: Session, dataset_id: UUID, sample_ids: list[UUID]) -> None:
    """Generate and store embeddings for samples.

    Args:
        session: Database session for resolver operations.
        dataset_id: The ID of the dataset to associate with the embedding model.
        sample_ids: List of sample IDs to generate embeddings for.
    """
    if not sample_ids:
        return

    embedding_manager = EmbeddingManagerProvider.get_embedding_manager()
    model_id = embedding_manager.load_or_get_default_model(
        session=session,
        dataset_id=dataset_id,
    )
    if model_id is None:
        print("No embedding model loaded. Skipping embedding generation.")
        return

    embedding_manager.embed_images(
        session=session,
        sample_ids=sample_ids,
        embedding_model_id=model_id,
    )

    # Mark the embedding search feature as enabled.
    if "embeddingSearchEnabled" not in features.lightly_studio_active_features:
        features.lightly_studio_active_features.append("embeddingSearchEnabled")
