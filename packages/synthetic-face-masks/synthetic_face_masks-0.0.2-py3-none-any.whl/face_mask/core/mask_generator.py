"""
Mask generation module for creating facial region masks.

This module provides the MaskGenerator class which handles:
- Creating masks for specific facial regions (eyes, mouth)
- Supporting both elliptical and rectangular mask shapes
- Generating region parameters for face mixing
"""

import cv2
import numpy as np
import random
from typing import Tuple, List, Optional, Dict, Any
from .face_processor import FaceProcessor
from ..utils.image_utils import ImageUtils, GeometryUtils


class RegionMask:
    """Data class to hold mask information for a facial region."""
    
    def __init__(self, center: Tuple[int, int], axis_h: int, axis_v: int, 
                 mask: np.ndarray, region_type: str):
        """
        Initialize a RegionMask.
        
        Args:
            center: Center point of the region (x, y)
            axis_h: Horizontal axis length
            axis_v: Vertical axis length
            mask: Binary mask for the region
            region_type: Type of region ('left_eye', 'right_eye', 'mouth')
        """
        self.center = center
        self.axis_h = axis_h
        self.axis_v = axis_v
        self.mask = mask
        self.region_type = region_type


class MaskGenerator:
    """
    Generates masks for facial regions using face landmarks.
    """
    
    def __init__(self, face_processor: FaceProcessor):
        """
        Initialize the MaskGenerator.
        
        Args:
            face_processor: FaceProcessor instance for landmark detection
        """
        self.face_processor = face_processor
    
    def create_ellipse_mask(self, image: np.ndarray, landmarks: List[Tuple[float, float]], 
                          mask: np.ndarray, scale_range: Tuple[float, float] = (0.9, 1.3)) -> Tuple[RegionMask, np.ndarray]:
        """
        Create an elliptical mask for a facial region.
        
        Args:
            image: Source image
            landmarks: Landmark points for the region
            mask: Existing mask to draw on
            scale_range: Random scaling range for the ellipse
            
        Returns:
            Tuple of (RegionMask object, updated mask)
        """
        # Calculate ellipse parameters
        center, axis_h, axis_v = GeometryUtils.calculate_ellipse_parameters(landmarks, scale_range)
        
        # Create the mask
        color = (255, 255, 255)
        annotated_image = image.copy()
        
        # Draw ellipse on both the annotation and mask
        cv2.ellipse(annotated_image, center, (axis_h, axis_v), 0, 0, 360, color, -1)
        cv2.ellipse(mask, center, (axis_h, axis_v), 0, 0, 360, color, -1)
        
        region_mask = RegionMask(center, axis_h, axis_v, mask.copy(), 'ellipse')
        
        return region_mask, mask
    
    def create_rectangle_mask(self, image: np.ndarray, landmarks: List[Tuple[float, float]], 
                            mask: np.ndarray, scale_range: Tuple[float, float] = (1.4, 1.8)) -> Tuple[RegionMask, np.ndarray]:
        """
        Create a rectangular mask for a facial region.
        
        Args:
            image: Source image
            landmarks: Landmark points for the region
            mask: Existing mask to draw on
            scale_range: Random scaling range for the rectangle
            
        Returns:
            Tuple of (RegionMask object, updated mask)
        """
        # Calculate rectangle parameters
        x1, y1, x2, y2 = GeometryUtils.calculate_rectangle_parameters(landmarks, scale_range)
        
        # Create the mask
        color = (255, 255, 255)
        annotated_image = image.copy()
        
        # Draw rectangle on both the annotation and mask
        cv2.rectangle(annotated_image, (x1, y1), (x2, y2), color, -1)
        cv2.rectangle(mask, (x1, y1), (x2, y2), color, -1)
        
        # Calculate center and axes for consistency
        center = ((x1 + x2) // 2, (y1 + y2) // 2)
        axis_h = x2 - x1
        axis_v = y2 - y1
        
        region_mask = RegionMask(center, axis_h, axis_v, mask.copy(), 'rectangle')
        
        return region_mask, mask
    
    def create_region_mask(self, image: np.ndarray, landmarks: List[Tuple[float, float]], 
                          mask: np.ndarray, is_ellipse: bool = True, 
                          region_type: str = 'unknown') -> Tuple[RegionMask, np.ndarray]:
        """
        Create a mask for a facial region.
        
        Args:
            image: Source image
            landmarks: Landmark points for the region
            mask: Existing mask to draw on
            is_ellipse: Whether to create ellipse (True) or rectangle (False)
            region_type: Type of region for identification
            
        Returns:
            Tuple of (RegionMask object, updated mask)
        """
        if is_ellipse:
            region_mask, updated_mask = self.create_ellipse_mask(image, landmarks, mask)
        else:
            region_mask, updated_mask = self.create_rectangle_mask(image, landmarks, mask)
        
        region_mask.region_type = region_type
        return region_mask, updated_mask
    
    def generate_face_masks(self, image_path: str, is_ellipse: bool = True, 
                          crop_border: int = 50, target_size: Tuple[int, int] = (320, 320)) -> Optional[Dict[str, Any]]:
        """
        Generate masks for all facial regions in an image.
        
        Args:
            image_path: Path to the input image
            is_ellipse: Whether to create elliptical or rectangular masks
            crop_border: Border pixels to crop
            target_size: Target image size
            
        Returns:
            Dictionary containing image, masks, and region parameters, or None if no face detected
        """
        # Process the image
        result = self.face_processor.process_image(image_path, crop_border, target_size)
        if result is None:
            return None
            
        image, face_results = result
        
        # Initialize mask
        mask = np.zeros_like(image)
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        
        # Get landmarks for all regions
        image_shape = image.shape[:2]  # (height, width)
        region_landmarks = self.face_processor.get_all_region_landmarks(face_results, image_shape)
        
        # Create masks for each region
        region_masks = {}
        annotated_image = image.copy()
        
        # Process left eye
        left_eye_mask, mask = self.create_region_mask(
            annotated_image, region_landmarks['left_eye'], mask, is_ellipse, 'left_eye'
        )
        region_masks['left_eye'] = left_eye_mask
        
        # Process right eye
        right_eye_mask, mask = self.create_region_mask(
            annotated_image, region_landmarks['right_eye'], mask, is_ellipse, 'right_eye'
        )
        region_masks['right_eye'] = right_eye_mask
        
        # Process mouth
        mouth_mask, mask = self.create_region_mask(
            annotated_image, region_landmarks['mouth'], mask, is_ellipse, 'mouth'
        )
        region_masks['mouth'] = mouth_mask
        
        return {
            'original_image': image,
            'annotated_image': annotated_image,
            'combined_mask': mask,
            'region_masks': region_masks,
            'face_results': face_results
        }
    
    def save_masks(self, mask_data: Dict[str, Any], output_dir: str, 
                  base_filename: str) -> Dict[str, str]:
        """
        Save generated masks to files.
        
        Args:
            mask_data: Dictionary returned by generate_face_masks
            output_dir: Directory to save masks
            base_filename: Base filename for output files
            
        Returns:
            Dictionary mapping mask types to saved file paths
        """
        import os
        
        saved_files = {}
        
        # Save annotated image
        annotated_path = os.path.join(output_dir, f"{base_filename}_annotated.png")
        cv2.imwrite(annotated_path, mask_data['annotated_image'])
        saved_files['annotated'] = annotated_path
        
        # Save combined mask
        mask_path = os.path.join(output_dir, f"{base_filename}_mask.png")
        cv2.imwrite(mask_path, mask_data['combined_mask'])
        saved_files['combined_mask'] = mask_path
        
        # Save individual region masks
        for region_name, region_mask in mask_data['region_masks'].items():
            region_path = os.path.join(output_dir, f"{base_filename}_{region_name}_mask.png")
            cv2.imwrite(region_path, region_mask.mask)
            saved_files[f"{region_name}_mask"] = region_path
        
        return saved_files
    
    def get_region_parameters(self, mask_data: Dict[str, Any]) -> Dict[str, Tuple[Tuple[int, int], int, int]]:
        """
        Extract region parameters from mask data.
        
        Args:
            mask_data: Dictionary returned by generate_face_masks
            
        Returns:
            Dictionary mapping region names to (center, axis_h, axis_v) tuples
        """
        parameters = {}
        
        for region_name, region_mask in mask_data['region_masks'].items():
            parameters[region_name] = (region_mask.center, region_mask.axis_h, region_mask.axis_v)
        
        return parameters
    
    def visualize_regions(self, mask_data: Dict[str, Any], show_landmarks: bool = True) -> np.ndarray:
        """
        Create a visualization of the detected regions.
        
        Args:
            mask_data: Dictionary returned by generate_face_masks
            show_landmarks: Whether to show face landmarks
            
        Returns:
            Visualization image
        """
        if show_landmarks:
            vis_image = self.face_processor.draw_landmarks(
                mask_data['original_image'], mask_data['face_results']
            )
        else:
            vis_image = mask_data['annotated_image'].copy()
        
        # Add region labels
        for region_name, region_mask in mask_data['region_masks'].items():
            center = region_mask.center
            cv2.putText(vis_image, region_name, (center[0] - 30, center[1] - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        
        return vis_image
