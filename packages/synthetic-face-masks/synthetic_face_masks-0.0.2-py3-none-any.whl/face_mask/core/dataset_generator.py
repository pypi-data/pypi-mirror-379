"""
Dataset generation module for orchestrating the face mixing pipeline.

This module provides the DatasetGenerator class which coordinates:
- Processing multiple face images
- Generating mixed images with different combinations
- Creating COCO format datasets
- Managing the complete dataset generation workflow
"""

import os
import random
import cv2
import numpy as np
from tqdm import tqdm
from typing import List, Dict, Any, Optional, Tuple
from .face_processor import FaceProcessor
from .mask_generator import MaskGenerator
from .image_mixer import ImageMixer
from ..utils.coco_utils import COCOUtils
from ..utils.image_utils import ImageUtils


class DatasetConfig:
    """Configuration class for dataset generation parameters."""
    
    def __init__(self,
                 input_folder: str,
                 output_folder: str,
                 background_folder: Optional[str] = None,
                 crop_border: int = 50,
                 target_size: Tuple[int, int] = (320, 320),
                 mix_probability: float = 0.5,
                 ellipse_probability: float = 0.5,
                 train_split_ratio: float = 0.8):
        """
        Initialize dataset generation configuration.
        
        Args:
            input_folder: Folder containing face images
            output_folder: Folder to save generated dataset
            background_folder: Optional folder containing background images
            crop_border: Border pixels to crop from input images
            target_size: Target size for processed images (width, height)
            mix_probability: Probability of creating mixed images vs normal images
            ellipse_probability: Probability of using ellipse vs rectangle masks
            train_split_ratio: Ratio for train/test split
        """
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.background_folder = background_folder
        self.crop_border = crop_border
        self.target_size = target_size
        self.mix_probability = mix_probability
        self.ellipse_probability = ellipse_probability
        self.train_split_ratio = train_split_ratio


class DatasetGenerator:
    """
    Main class for orchestrating face mixing dataset generation.
    """
    
    def __init__(self, config: DatasetConfig):
        """
        Initialize the DatasetGenerator.
        
        Args:
            config: Dataset generation configuration
        """
        self.config = config
        self.face_processor = FaceProcessor()
        self.mask_generator = MaskGenerator(self.face_processor)
        self.image_mixer = ImageMixer(self.mask_generator)
        self.coco_utils = COCOUtils()
        
        # Create output directories
        self.images_dir = os.path.join(config.output_folder, "images")
        self.annotations_dir = os.path.join(config.output_folder, "annotations")
        os.makedirs(self.images_dir, exist_ok=True)
        os.makedirs(self.annotations_dir, exist_ok=True)
        
        # Initialize tracking variables
        self.image_annotations = []
        self.object_annotations = []
        self.current_id = 0
    
    def get_face_image_paths(self) -> List[str]:
        """
        Get all face image paths from input folder.
        
        Returns:
            List of image file paths
        """
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
        image_paths = []
        
        if os.path.isdir(self.config.input_folder):
            # If input is a directory with subdirectories (like GANImages)
            for root, dirs, files in os.walk(self.config.input_folder):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in image_extensions):
                        image_paths.append(os.path.join(root, file))
        else:
            raise ValueError(f"Input folder does not exist: {self.config.input_folder}")
        
        return image_paths
    
    def get_background_image_paths(self) -> List[str]:
        """
        Get all background image paths.
        
        Returns:
            List of background image file paths
        """
        if not self.config.background_folder or not os.path.exists(self.config.background_folder):
            return []
        
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
        bg_paths = []
        
        for file in os.listdir(self.config.background_folder):
            if any(file.lower().endswith(ext) for ext in image_extensions):
                bg_paths.append(os.path.join(self.config.background_folder, file))
        
        return bg_paths
    
    def generate_normal_image(self, image_path: str, output_filename: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Process a normal (non-mixed) image and generate annotations.
        
        Args:
            image_path: Path to the input image
            output_filename: Name for the output file
            
        Returns:
            Tuple of (image_annotation, object_annotation)
        """
        # Load and process image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Could not load image: {image_path}")
        
        # Apply basic processing
        processed_image = ImageUtils.crop_image(image, self.config.crop_border)
        processed_image = ImageUtils.resize_image_with_aspect(processed_image, self.config.target_size)
        
        # Save processed image
        output_path = os.path.join(self.images_dir, output_filename)
        cv2.imwrite(output_path, processed_image)
        
        # Generate annotations (category_id=1 for normal images)
        self.current_id += 1
        return self.coco_utils.generate_coco_annotations(output_filename, self.current_id, 1)
    
    def generate_mixed_images(self, target_path: str, source_paths: List[str], 
                            bg_paths: List[str], base_name: str) -> List[Tuple[Dict[str, Any], Dict[str, Any]]]:
        """
        Generate mixed images with different facial region combinations.
        
        Args:
            target_path: Path to target face image
            source_paths: List of source face image paths for mixing
            bg_paths: List of background image paths
            base_name: Base name for output files
            
        Returns:
            List of annotation tuples for generated images
        """
        annotations = []
        
        # Choose random background if available
        bg_image = None
        if bg_paths:
            bg_path = random.choice(bg_paths)
            bg_image = cv2.imread(bg_path)
        
        # Determine mask type
        is_ellipse = random.random() < self.config.ellipse_probability
        
        # Generate target mask data
        target_data = self.mask_generator.generate_face_masks(
            target_path, is_ellipse, self.config.crop_border, self.config.target_size
        )
        
        if target_data is None:
            return annotations
        
        # Generate normal target image first
        self.current_id += 1
        normal_filename = f"{base_name}.png"
        normal_path = os.path.join(self.images_dir, normal_filename)
        cv2.imwrite(normal_path, target_data['original_image'])
        annotations.append(self.coco_utils.generate_coco_annotations(normal_filename, self.current_id, 1))
        
        # Ensure we have enough source images
        if len(source_paths) < 3:
            return annotations
        
        # Select different source images for different regions
        available_indices = list(range(len(source_paths)))
        
        try:
            # Source for eyes
            eye_source_idx = ImageUtils.conditional_random_number(len(source_paths), [])
            eye_source_data = self.mask_generator.generate_face_masks(
                source_paths[eye_source_idx], is_ellipse, self.config.crop_border, self.config.target_size
            )
            
            if eye_source_data is not None:
                # Generate eye-mixed images
                eye_mix_result = self.image_mixer.mix_images(
                    eye_source_data, target_data, bg_image, mix_eyes=True, mix_mouth=False
                )
                
                # Save eye-mixed image
                self.current_id += 1
                eye_filename = f"{base_name}-Eye.png"
                eye_path = os.path.join(self.images_dir, eye_filename)
                cv2.imwrite(eye_path, eye_mix_result.mixed_image)
                annotations.append(self.coco_utils.generate_coco_annotations(eye_filename, self.current_id, 2))
                
                # Save eye-background mixed image
                if eye_mix_result.mixed_bg_image is not None:
                    self.current_id += 1
                    eye_bg_filename = f"{base_name}-EyeBG.png"
                    eye_bg_path = os.path.join(self.images_dir, eye_bg_filename)
                    cv2.imwrite(eye_bg_path, eye_mix_result.mixed_bg_image)
                    annotations.append(self.coco_utils.generate_coco_annotations(eye_bg_filename, self.current_id, 2))
            
            # Source for mouth
            mouth_source_idx = ImageUtils.conditional_random_number(len(source_paths), [eye_source_idx])
            mouth_source_data = self.mask_generator.generate_face_masks(
                source_paths[mouth_source_idx], is_ellipse, self.config.crop_border, self.config.target_size
            )
            
            if mouth_source_data is not None:
                # Generate mouth-mixed images
                mouth_mix_result = self.image_mixer.mix_images(
                    mouth_source_data, target_data, bg_image, mix_eyes=False, mix_mouth=True
                )
                
                # Save mouth-mixed image
                self.current_id += 1
                mouth_filename = f"{base_name}-Mouth.png"
                mouth_path = os.path.join(self.images_dir, mouth_filename)
                cv2.imwrite(mouth_path, mouth_mix_result.mixed_image)
                annotations.append(self.coco_utils.generate_coco_annotations(mouth_filename, self.current_id, 2))
                
                # Save mouth-background mixed image
                if mouth_mix_result.mixed_bg_image is not None:
                    self.current_id += 1
                    mouth_bg_filename = f"{base_name}-MouthBG.png"
                    mouth_bg_path = os.path.join(self.images_dir, mouth_bg_filename)
                    cv2.imwrite(mouth_bg_path, mouth_mix_result.mixed_bg_image)
                    annotations.append(self.coco_utils.generate_coco_annotations(mouth_bg_filename, self.current_id, 2))
            
            # Source for full face mixing
            full_source_idx = ImageUtils.conditional_random_number(len(source_paths), [eye_source_idx, mouth_source_idx])
            full_source_data = self.mask_generator.generate_face_masks(
                source_paths[full_source_idx], is_ellipse, self.config.crop_border, self.config.target_size
            )
            
            if full_source_data is not None:
                # Generate full-mixed images
                full_mix_result = self.image_mixer.mix_images(
                    full_source_data, target_data, bg_image, mix_eyes=True, mix_mouth=True
                )
                
                # Save full-mixed image
                self.current_id += 1
                full_filename = f"{base_name}-Both.png"
                full_path = os.path.join(self.images_dir, full_filename)
                cv2.imwrite(full_path, full_mix_result.mixed_image)
                annotations.append(self.coco_utils.generate_coco_annotations(full_filename, self.current_id, 2))
                
                # Save full-background mixed image
                if full_mix_result.mixed_bg_image is not None:
                    self.current_id += 1
                    full_bg_filename = f"{base_name}-BothBG.png"
                    full_bg_path = os.path.join(self.images_dir, full_bg_filename)
                    cv2.imwrite(full_bg_path, full_mix_result.mixed_bg_image)
                    annotations.append(self.coco_utils.generate_coco_annotations(full_bg_filename, self.current_id, 2))
        
        except Exception as e:
            print(f"Error generating mixed images for {base_name}: {str(e)}")
        
        return annotations
    
    def generate_dataset(self) -> Dict[str, Any]:
        """
        Generate the complete dataset.
        
        Returns:
            Dictionary with generation statistics
        """
        # Get all image paths
        face_paths = self.get_face_image_paths()
        bg_paths = self.get_background_image_paths()
        
        print(f"Found {len(face_paths)} face images")
        print(f"Found {len(bg_paths)} background images")
        
        if not face_paths:
            raise ValueError("No face images found in input folder")
        
        # Sample face images for mixing
        sampled_faces = random.sample(face_paths, min(len(face_paths), 1000))  # Limit for performance
        
        # Generate dataset
        stats = {"normal_images": 0, "mixed_images": 0, "failed_images": 0}
        
        for idx, face_path in enumerate(tqdm(sampled_faces, desc="Generating dataset")):
            try:
                # Extract base name from path
                base_name = os.path.splitext(os.path.basename(face_path))[0]
                base_name = f"img_{idx:06d}"  # Use consistent naming
                
                # Decide whether to create mixed images or just normal image
                if random.random() < self.config.mix_probability and len(sampled_faces) > 3:
                    # Generate mixed images
                    exclude_current = [idx]
                    available_sources = [path for i, path in enumerate(sampled_faces) if i not in exclude_current]
                    
                    if len(available_sources) >= 3:
                        annotations_list = self.generate_mixed_images(
                            face_path, available_sources, bg_paths, base_name
                        )
                        
                        # Add annotations
                        for img_ann, obj_ann in annotations_list:
                            self.image_annotations.append(img_ann)
                            self.object_annotations.append(obj_ann)
                        
                        stats["mixed_images"] += len(annotations_list)
                    else:
                        # Fall back to normal image
                        normal_filename = f"{base_name}.png"
                        img_ann, obj_ann = self.generate_normal_image(face_path, normal_filename)
                        self.image_annotations.append(img_ann)
                        self.object_annotations.append(obj_ann)
                        stats["normal_images"] += 1
                else:
                    # Generate normal image
                    normal_filename = f"{base_name}.png"
                    img_ann, obj_ann = self.generate_normal_image(face_path, normal_filename)
                    self.image_annotations.append(img_ann)
                    self.object_annotations.append(obj_ann)
                    stats["normal_images"] += 1
                    
            except Exception as e:
                print(f"Failed to process {face_path}: {str(e)}")
                stats["failed_images"] += 1
                continue
        
        # Create and save COCO dataset
        coco_dataset = self.coco_utils.create_coco_dataset(
            self.image_annotations, self.object_annotations
        )
        
        # Save main annotations
        main_annotations_path = os.path.join(self.annotations_dir, "annotations.json")
        self.coco_utils.save_coco_annotations(coco_dataset, main_annotations_path)
        
        # Create train/test split
        train_path = os.path.join(self.annotations_dir, "train.json")
        test_path = os.path.join(self.annotations_dir, "test.json")
        self.coco_utils.split_coco_dataset(
            main_annotations_path, train_path, test_path, self.config.train_split_ratio
        )
        
        stats["total_images"] = len(self.image_annotations)
        stats["output_folder"] = self.config.output_folder
        
        return stats
    
    def validate_dataset(self) -> Dict[str, Any]:
        """
        Validate the generated dataset.
        
        Returns:
            Validation results
        """
        annotations_path = os.path.join(self.annotations_dir, "annotations.json")
        if os.path.exists(annotations_path):
            return self.coco_utils.validate_coco_dataset(annotations_path)
        else:
            return {"valid": False, "error": "No annotations file found"}
    
    def generate_report(self) -> None:
        """Generate a dataset report."""
        from ..utils.coco_utils import DatasetMetrics
        
        annotations_path = os.path.join(self.annotations_dir, "annotations.json")
        report_path = os.path.join(self.config.output_folder, "dataset_report.json")
        
        if os.path.exists(annotations_path):
            DatasetMetrics.generate_dataset_report(annotations_path, report_path)
        else:
            print("No annotations file found for report generation")
