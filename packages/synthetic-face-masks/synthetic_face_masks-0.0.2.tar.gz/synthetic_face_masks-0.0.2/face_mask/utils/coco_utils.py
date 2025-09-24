"""
COCO annotation utilities for dataset generation and management.

This module provides utilities for:
- Generating COCO format annotations
- Creating dataset splits (train/test)
- Managing image metadata
"""

import json
import os
import random
from datetime import datetime
from typing import List, Dict, Any, Tuple, Optional


class COCOUtils:
    """
    Utilities for creating and managing COCO format annotations.
    """
    
    def __init__(self):
        """Initialize COCOUtils with default COCO structure."""
        self.base_coco_structure = {
            "info": {
                "description": "Face Mixing Dataset",
                "version": "1.0",
                "year": datetime.now().year,
                "contributor": "Face Mixing Project",
                "date_created": datetime.now().strftime("%Y-%m-%d")
            },
            "licenses": [
                {
                    "id": 1,
                    "name": "Custom License",
                    "url": ""
                }
            ],
            "categories": [
                {
                    "id": 1,
                    "name": "normal_image",
                    "supercategory": "face"
                },
                {
                    "id": 2,
                    "name": "mixed_image",
                    "supercategory": "face"
                }
            ]
        }
    
    def generate_image_annotation(self, image_id: int, filename: str, 
                                width: int = 320, height: int = 320) -> Dict[str, Any]:
        """
        Generate COCO image annotation.
        
        Args:
            image_id: Unique image identifier
            filename: Name of the image file
            width: Image width
            height: Image height
            
        Returns:
            COCO image annotation dictionary
        """
        return {
            "id": image_id,
            "width": width,
            "height": height,
            "file_name": filename,
            "license": 1,
            "date_captured": datetime.now().strftime("%Y-%m-%d")
        }
    
    def generate_object_annotation(self, annotation_id: int, image_id: int, 
                                 category_id: int, width: int = 320, 
                                 height: int = 320) -> Dict[str, Any]:
        """
        Generate COCO object annotation.
        
        Args:
            annotation_id: Unique annotation identifier
            image_id: Image ID this annotation belongs to
            category_id: Category ID (1=normal, 2=mixed)
            width: Image width
            height: Image height
            
        Returns:
            COCO object annotation dictionary
        """
        return {
            "id": annotation_id,
            "image_id": image_id,
            "category_id": category_id,
            "bbox": [0, 0, width, height],  # Full image bounding box
            "area": width * height,
            "segmentation": [],
            "iscrowd": 0
        }
    
    def generate_coco_annotations(self, image_filename: str, image_id: int, 
                                category_id: int) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Generate both image and object annotations for a single image.
        
        Args:
            image_filename: Name of the image file
            image_id: Unique image identifier
            category_id: Category ID (1=normal, 2=mixed)
            
        Returns:
            Tuple of (image_annotation, object_annotation)
        """
        image_annotation = self.generate_image_annotation(image_id, image_filename)
        object_annotation = self.generate_object_annotation(image_id, image_id, category_id)
        
        return image_annotation, object_annotation
    
    def create_coco_dataset(self, image_annotations: List[Dict[str, Any]], 
                          object_annotations: List[Dict[str, Any]], 
                          custom_info: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Create complete COCO dataset structure.
        
        Args:
            image_annotations: List of image annotations
            object_annotations: List of object annotations
            custom_info: Optional custom info to override defaults
            
        Returns:
            Complete COCO dataset dictionary
        """
        coco_dataset = self.base_coco_structure.copy()
        
        if custom_info:
            coco_dataset["info"].update(custom_info)
        
        coco_dataset["images"] = image_annotations
        coco_dataset["annotations"] = object_annotations
        
        return coco_dataset
    
    def save_coco_annotations(self, coco_dataset: Dict[str, Any], 
                            output_path: str) -> None:
        """
        Save COCO dataset to JSON file.
        
        Args:
            coco_dataset: Complete COCO dataset dictionary
            output_path: Path to save the JSON file
        """
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(coco_dataset, f, indent=4)
        
        print(f"COCO annotations saved to: {output_path}")
    
    def split_coco_dataset(self, annotation_file: str, train_file: str, 
                         test_file: str, train_ratio: float = 0.8) -> None:
        """
        Split COCO annotation file into train and test sets.
        
        Args:
            annotation_file: Path to the original annotation file
            train_file: Path for the training set output
            test_file: Path for the test set output
            train_ratio: Ratio of images for training (0.0 to 1.0)
        """
        # Load original annotations
        with open(annotation_file, 'r') as f:
            coco_data = json.load(f)
        
        # Extract images and annotations
        images = coco_data['images']
        annotations = coco_data['annotations']
        
        # Create base structure for both splits
        train_data = {
            "info": coco_data.get("info", {}),
            "licenses": coco_data.get("licenses", []),
            "images": [],
            "annotations": [],
            "categories": coco_data.get("categories", [])
        }
        test_data = train_data.copy()
        test_data["images"] = []
        test_data["annotations"] = []
        
        # Shuffle and split images
        random.shuffle(images)
        num_train_images = int(train_ratio * len(images))
        train_images = images[:num_train_images]
        test_images = images[num_train_images:]
        
        # Create sets of image IDs
        train_image_ids = set(img['id'] for img in train_images)
        test_image_ids = set(img['id'] for img in test_images)
        
        # Assign images to respective datasets
        train_data['images'] = train_images
        test_data['images'] = test_images
        
        # Split annotations based on image IDs
        for annotation in annotations:
            if annotation['image_id'] in train_image_ids:
                train_data['annotations'].append(annotation)
            elif annotation['image_id'] in test_image_ids:
                test_data['annotations'].append(annotation)
        
        # Save split datasets
        with open(train_file, 'w') as f:
            json.dump(train_data, f, indent=4)
        
        with open(test_file, 'w') as f:
            json.dump(test_data, f, indent=4)
        
        print(f"Training annotations saved to: {train_file}")
        print(f"Test annotations saved to: {test_file}")
        print(f"Train images: {len(train_images)}, Test images: {len(test_images)}")
    
    def validate_coco_dataset(self, annotation_file: str) -> Dict[str, Any]:
        """
        Validate COCO dataset structure and return statistics.
        
        Args:
            annotation_file: Path to the annotation file
            
        Returns:
            Dictionary with validation results and statistics
        """
        try:
            with open(annotation_file, 'r') as f:
                coco_data = json.load(f)
        except Exception as e:
            return {"valid": False, "error": f"Failed to load JSON: {str(e)}"}
        
        # Check required fields
        required_fields = ["info", "licenses", "categories", "images", "annotations"]
        missing_fields = [field for field in required_fields if field not in coco_data]
        
        if missing_fields:
            return {"valid": False, "error": f"Missing required fields: {missing_fields}"}
        
        # Collect statistics
        stats = {
            "valid": True,
            "num_images": len(coco_data["images"]),
            "num_annotations": len(coco_data["annotations"]),
            "num_categories": len(coco_data["categories"]),
            "categories": [cat["name"] for cat in coco_data["categories"]]
        }
        
        # Check for image-annotation consistency
        image_ids = set(img["id"] for img in coco_data["images"])
        annotation_image_ids = set(ann["image_id"] for ann in coco_data["annotations"])
        
        orphaned_annotations = annotation_image_ids - image_ids
        if orphaned_annotations:
            stats["warnings"] = [f"Found {len(orphaned_annotations)} annotations with no corresponding images"]
        
        return stats
    
    def merge_coco_datasets(self, dataset_files: List[str], output_file: str) -> None:
        """
        Merge multiple COCO dataset files into one.
        
        Args:
            dataset_files: List of paths to COCO dataset files
            output_file: Path for the merged output file
        """
        if not dataset_files:
            raise ValueError("No dataset files provided")
        
        # Load first dataset as base
        with open(dataset_files[0], 'r') as f:
            merged_data = json.load(f)
        
        # Track max IDs to avoid conflicts
        max_image_id = max(img["id"] for img in merged_data["images"]) if merged_data["images"] else 0
        max_annotation_id = max(ann["id"] for ann in merged_data["annotations"]) if merged_data["annotations"] else 0
        
        # Merge remaining datasets
        for dataset_file in dataset_files[1:]:
            with open(dataset_file, 'r') as f:
                data = json.load(f)
            
            # Update image IDs and add images
            for img in data["images"]:
                old_id = img["id"]
                max_image_id += 1
                img["id"] = max_image_id
                merged_data["images"].append(img)
                
                # Update corresponding annotations
                for ann in data["annotations"]:
                    if ann["image_id"] == old_id:
                        max_annotation_id += 1
                        ann["id"] = max_annotation_id
                        ann["image_id"] = max_image_id
                        merged_data["annotations"].append(ann)
        
        # Save merged dataset
        self.save_coco_annotations(merged_data, output_file)
        print(f"Merged {len(dataset_files)} datasets into {output_file}")


class DatasetMetrics:
    """Utilities for analyzing dataset metrics and statistics."""
    
    @staticmethod
    def analyze_dataset(annotation_file: str) -> Dict[str, Any]:
        """
        Analyze COCO dataset and return detailed metrics.
        
        Args:
            annotation_file: Path to the annotation file
            
        Returns:
            Dictionary with detailed dataset metrics
        """
        with open(annotation_file, 'r') as f:
            coco_data = json.load(f)
        
        images = coco_data["images"]
        annotations = coco_data["annotations"]
        categories = coco_data["categories"]
        
        # Basic counts
        metrics = {
            "total_images": len(images),
            "total_annotations": len(annotations),
            "total_categories": len(categories)
        }
        
        # Category distribution
        category_counts = {}
        for ann in annotations:
            cat_id = ann["category_id"]
            cat_name = next((cat["name"] for cat in categories if cat["id"] == cat_id), f"Category_{cat_id}")
            category_counts[cat_name] = category_counts.get(cat_name, 0) + 1
        
        metrics["category_distribution"] = category_counts
        
        # Image dimensions analysis
        widths = [img["width"] for img in images]
        heights = [img["height"] for img in images]
        
        metrics["image_dimensions"] = {
            "unique_widths": list(set(widths)),
            "unique_heights": list(set(heights)),
            "most_common_size": f"{max(set(widths), key=widths.count)}x{max(set(heights), key=heights.count)}"
        }
        
        return metrics
    
    @staticmethod
    def generate_dataset_report(annotation_file: str, output_file: str) -> None:
        """
        Generate a detailed dataset report.
        
        Args:
            annotation_file: Path to the annotation file
            output_file: Path for the report output
        """
        coco_utils = COCOUtils()
        validation = coco_utils.validate_coco_dataset(annotation_file)
        metrics = DatasetMetrics.analyze_dataset(annotation_file)
        
        report = {
            "dataset_file": annotation_file,
            "validation": validation,
            "metrics": metrics,
            "generated_at": datetime.now().isoformat()
        }
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=4)
        
        print(f"Dataset report saved to: {output_file}")
