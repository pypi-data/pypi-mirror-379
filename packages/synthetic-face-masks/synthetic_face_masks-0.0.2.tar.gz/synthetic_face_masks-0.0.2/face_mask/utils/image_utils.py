"""
Image utilities module containing helper functions for image processing.

This module provides utility functions for:
- Image cropping and resizing
- Image augmentation
- Geometric calculations (distance, line intersection)
- Coordinate transformations
"""

import cv2
import numpy as np
import random
import imgaug.augmenters as iaa
from typing import Tuple, List, Optional


class ImageUtils:
    """Utility class for image processing operations."""
    
    @staticmethod
    def crop_image(image: np.ndarray, border_size: int) -> np.ndarray:
        """
        Crop image by removing border pixels from all sides.
        
        Args:
            image: Input image as numpy array
            border_size: Number of pixels to remove from each side
            
        Returns:
            Cropped image
        """
        height, width = image.shape[:2]
        return image[border_size:height-border_size, border_size:width-border_size]
    
    @staticmethod
    def augment_image(image: np.ndarray, noise_scale: float = 0.035, 
                     blur_sigma: Tuple[float, float] = (0, 1.5)) -> np.ndarray:
        """
        Apply augmentation to image with noise and blur.
        
        Args:
            image: Input image
            noise_scale: Scale for Gaussian noise (relative to 255)
            blur_sigma: Range for Gaussian blur sigma
            
        Returns:
            Augmented image
        """
        seq = iaa.Sequential([
            iaa.AdditiveGaussianNoise(scale=(noise_scale * 255)),
            iaa.GaussianBlur(sigma=blur_sigma)
        ])
        return seq(image=image)
    
    @staticmethod
    def line_intersection(line1: Tuple[Tuple[float, float], Tuple[float, float]], 
                         line2: Tuple[Tuple[float, float], Tuple[float, float]]) -> Tuple[int, int]:
        """
        Find intersection point of two lines.
        
        Args:
            line1: First line as ((x1, y1), (x2, y2))
            line2: Second line as ((x1, y1), (x2, y2))
            
        Returns:
            Intersection point as (y, x) - Note: returns y, x format
            
        Raises:
            Exception: If lines do not intersect (parallel lines)
        """
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a: Tuple[float, float], b: Tuple[float, float]) -> float:
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            raise Exception('Lines do not intersect')

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return int(y), int(x)
    
    @staticmethod
    def get_distance(pt1: Tuple[float, float], pt2: Tuple[float, float]) -> int:
        """
        Calculate Euclidean distance between two points, divided by 2.
        
        Args:
            pt1: First point (x, y)
            pt2: Second point (x, y)
            
        Returns:
            Distance between points divided by 2
        """
        return int(np.sqrt(np.square(pt1[0] - pt2[0]) + np.square(pt1[1] - pt2[1])) / 2)
    
    @staticmethod
    def landmark_to_pts(landmark, shape: Tuple[int, int]) -> Tuple[float, float]:
        """
        Convert MediaPipe landmark to pixel coordinates.
        
        Args:
            landmark: MediaPipe landmark object
            shape: Image shape (height, width)
            
        Returns:
            Pixel coordinates as (y, x) - Note: returns y, x format
        """
        return (landmark.y * shape[0], landmark.x * shape[1])
    
    @staticmethod
    def resize_image_with_aspect(image: np.ndarray, target_size: Tuple[int, int], 
                               interpolation: int = cv2.INTER_NEAREST) -> np.ndarray:
        """
        Resize image to target size.
        
        Args:
            image: Input image
            target_size: Target size as (width, height)
            interpolation: OpenCV interpolation method
            
        Returns:
            Resized image
        """
        return cv2.resize(image, target_size, interpolation=interpolation)
    
    @staticmethod
    def conditional_random_number(total_num: int, exclude_list: List[int]) -> int:
        """
        Generate random number excluding specified values.
        
        Args:
            total_num: Upper bound for random number generation
            exclude_list: List of numbers to exclude
            
        Returns:
            Random number not in exclude_list
        """
        numbers = [i for i in range(0, total_num - 1) if i not in exclude_list]
        return random.choice(numbers)
    
    @staticmethod
    def create_blurred_mask(mask: np.ndarray, blur_kernel_size: int) -> np.ndarray:
        """
        Create a blurred version of the mask for smooth blending.
        
        Args:
            mask: Input mask as grayscale or BGR image
            blur_kernel_size: Size of Gaussian blur kernel (must be odd)
            
        Returns:
            Blurred mask normalized to [0, 1] range
        """
        if len(mask.shape) == 3:
            mask_blur = cv2.GaussianBlur(mask, (blur_kernel_size, blur_kernel_size), 0)
        else:
            mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
            mask_blur = cv2.GaussianBlur(mask_bgr, (blur_kernel_size, blur_kernel_size), 0)
        
        combined_mask = mask_blur + mask
        return combined_mask.astype(np.float32) / 255.0


class GeometryUtils:
    """Utility class for geometric operations on facial features."""
    
    @staticmethod
    def calculate_ellipse_parameters(points: List[Tuple[float, float]], 
                                   scale_range: Tuple[float, float] = (0.9, 1.3)) -> Tuple[Tuple[int, int], int, int]:
        """
        Calculate ellipse parameters from facial landmark points.
        
        Args:
            points: List of 6 points defining the region in notebook order [tl, br, tr, bl, eL, eR]
            scale_range: Range for random scaling factor
            
        Returns:
            Tuple of (center_point, horizontal_axis, vertical_axis)
        """
        # Notebook order: [tl, br, tr, bl, eL, eR]
        tl, br, tr, bl, eL, eR = points
        
        # Use direct line intersection - match exact notebook behavior
        center = ImageUtils.line_intersection((tl, br), (tr, bl))
        
        scale = random.uniform(*scale_range)
        axis_h = int(ImageUtils.get_distance(eL, eR) * scale)
        axis_v = int(ImageUtils.get_distance(tl, br) * scale)
        
        return center, axis_h, axis_v
    
    @staticmethod
    def calculate_rectangle_parameters(points: List[Tuple[float, float]], 
                                     scale_range: Tuple[float, float] = (1.4, 1.8)) -> Tuple[int, int, int, int]:
        """
        Calculate rectangle parameters from facial landmark points.
        
        Args:
            points: List of 6 points defining the region in notebook order [tl, br, tr, bl, eL, eR]
            scale_range: Range for random scaling factor
            
        Returns:
            Rectangle coordinates as (x1, y1, x2, y2)
        """
        # Notebook order: [tl, br, tr, bl, eL, eR]
        tl, br, tr, bl, eL, eR = points
        center = ImageUtils.line_intersection((tl, br), (tr, bl))
        
        scale = random.uniform(*scale_range)
        axis_h = int(ImageUtils.get_distance(eL, eR) * scale * 1.2)
        axis_v = int(ImageUtils.get_distance(tl, br) * scale * 1.2)
        
        cx, cy = center
        x1 = int(cx - axis_h // 2)
        y1 = int(cy - axis_v // 2)
        x2 = int(cx + axis_h // 2)
        y2 = int(cy + axis_v // 2)
        
        return x1, y1, x2, y2
