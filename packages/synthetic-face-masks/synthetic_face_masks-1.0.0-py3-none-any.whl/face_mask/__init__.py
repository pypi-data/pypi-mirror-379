"""
Face Mixing Project - A library for generating synthetic face datasets.

This package provides tools for:
- Face landmark detection and processing
- Creating facial region masks
- Mixing and blending face images
- Generating COCO format datasets

Author: Your Name
License: MIT
"""

from .core.face_processor import FaceProcessor
from .core.mask_generator import MaskGenerator
from .core.image_mixer import ImageMixer
from .core.dataset_generator import DatasetGenerator
from .utils.coco_utils import COCOUtils
from .utils.image_utils import ImageUtils

__version__ = "1.0.0"
__author__ = "Your Name"

__all__ = [
    "FaceProcessor",
    "MaskGenerator", 
    "ImageMixer",
    "DatasetGenerator",
    "COCOUtils",
    "ImageUtils"
]
