"""
Face processing module for landmark detection and facial region extraction.

This module provides the FaceProcessor class which handles:
- Face mesh detection using MediaPipe
- Facial landmark extraction
- Region-specific processing for eyes and mouth
"""

import cv2
import mediapipe as mp
import numpy as np
from typing import Tuple, List, Optional, Dict, Any
from ..utils.image_utils import ImageUtils, GeometryUtils


class FaceProcessor:
    """
    Handles face detection and landmark processing using MediaPipe Face Mesh.
    """
    
    def __init__(self, 
                 static_image_mode: bool = True, 
                 min_detection_confidence: float = 0.5,
                 max_num_faces: int = 1):
        """
        Initialize the FaceProcessor.
        
        Args:
            static_image_mode: Whether to process static images or video stream
            min_detection_confidence: Minimum confidence for face detection
            max_num_faces: Maximum number of faces to detect
        """
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_face_mesh = mp.solutions.face_mesh
        self.static_image_mode = static_image_mode
        self.min_detection_confidence = min_detection_confidence
        self.max_num_faces = max_num_faces
        
        # Define landmark indices for facial regions
        self.landmark_indices = {
            'left_eye': [224, 22, 222, 144, 226, 245],
            'right_eye': [442, 254, 444, 252, 465, 446],
            'mouth': [37, 314, 267, 84, 57, 287]
        }
    
    def process_image(self, image_path: str, crop_border: int = 50, 
                     target_size: Tuple[int, int] = (320, 320)) -> Optional[Tuple[np.ndarray, Any]]:
        """
        Process an image to extract face landmarks.
        
        Args:
            image_path: Path to the input image
            crop_border: Number of pixels to crop from borders
            target_size: Target size for resizing (width, height)
            
        Returns:
            Tuple of (processed_image, face_mesh_results) or None if no face detected
        """
        # Load and preprocess image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Could not load image from {image_path}")
            
        image = ImageUtils.crop_image(image, crop_border)
        image = ImageUtils.resize_image_with_aspect(image, target_size)
        
        # Process with MediaPipe
        with self.mp_face_mesh.FaceMesh(
            static_image_mode=self.static_image_mode,
            max_num_faces=self.max_num_faces,
            min_detection_confidence=self.min_detection_confidence
        ) as face_mesh:
            # Convert BGR to RGB
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(rgb_image)
            
            if not results.multi_face_landmarks:
                return None
                
            return image, results
    
    def extract_region_landmarks(self, results: Any, region: str, 
                               image_shape: Tuple[int, int]) -> List[Tuple[float, float]]:
        """
        Extract landmark points for a specific facial region.
        
        Args:
            results: MediaPipe face mesh results
            region: Region name ('left_eye', 'right_eye', 'mouth')
            image_shape: Shape of the image (height, width)
            
        Returns:
            List of landmark points as (y, x) coordinates
        """
        if region not in self.landmark_indices:
            raise ValueError(f"Unknown region: {region}. Available: {list(self.landmark_indices.keys())}")
        
        points = []
        landmark_list = self.landmark_indices[region]
        
        for landmark_idx in landmark_list:
            landmark = results.multi_face_landmarks[0].landmark[landmark_idx]
            point = ImageUtils.landmark_to_pts(landmark, image_shape)
            points.append(point)
            
        return points
    
    def get_all_region_landmarks(self, results: Any, 
                               image_shape: Tuple[int, int]) -> Dict[str, List[Tuple[float, float]]]:
        """
        Extract landmarks for all facial regions.
        
        Args:
            results: MediaPipe face mesh results
            image_shape: Shape of the image (height, width)
            
        Returns:
            Dictionary mapping region names to landmark points
        """
        region_landmarks = {}
        
        for region in self.landmark_indices.keys():
            region_landmarks[region] = self.extract_region_landmarks(results, region, image_shape)
            
        return region_landmarks
    
    def calculate_region_parameters(self, landmarks: List[Tuple[float, float]], 
                                  is_ellipse: bool = True) -> Tuple[Tuple[int, int], int, int]:
        """
        Calculate geometric parameters for a facial region.
        
        Args:
            landmarks: List of landmark points for the region
            is_ellipse: Whether to calculate ellipse or rectangle parameters
            
        Returns:
            Tuple of (center, horizontal_axis, vertical_axis)
        """
        if is_ellipse:
            center, axis_h, axis_v = GeometryUtils.calculate_ellipse_parameters(landmarks)
        else:
            x1, y1, x2, y2 = GeometryUtils.calculate_rectangle_parameters(landmarks)
            center = ((x1 + x2) // 2, (y1 + y2) // 2)
            axis_h = x2 - x1
            axis_v = y2 - y1
            
        return center, axis_h, axis_v
    
    def draw_landmarks(self, image: np.ndarray, results: Any, 
                      drawing_spec: Optional[Any] = None) -> np.ndarray:
        """
        Draw face mesh landmarks on the image.
        
        Args:
            image: Input image
            results: MediaPipe face mesh results
            drawing_spec: Drawing specifications
            
        Returns:
            Image with landmarks drawn
        """
        if drawing_spec is None:
            drawing_spec = self.mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
            
        annotated_image = image.copy()
        
        for face_landmarks in results.multi_face_landmarks:
            self.mp_drawing.draw_landmarks(
                image=annotated_image,
                landmark_list=face_landmarks,
                connections=self.mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=None,
                connection_drawing_spec=drawing_spec
            )
            
        return annotated_image
    
    def validate_face_detection(self, results: Any) -> bool:
        """
        Validate that face detection was successful.
        
        Args:
            results: MediaPipe face mesh results
            
        Returns:
            True if at least one face was detected
        """
        return results.multi_face_landmarks is not None and len(results.multi_face_landmarks) > 0
