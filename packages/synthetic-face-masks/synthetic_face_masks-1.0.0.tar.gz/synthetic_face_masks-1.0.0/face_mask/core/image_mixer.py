"""
Image mixing module for blending facial regions between different images.

This module provides the ImageMixer class which handles:
- Mixing facial regions between source and target images
- Scaling and positioning operations for region matching
- Blending with background images
- Creating smooth transitions using masks
"""

import cv2
import numpy as np
import random
from typing import Tuple, List, Optional, Dict, Any, Union
from .mask_generator import MaskGenerator, RegionMask
from ..utils.image_utils import ImageUtils


class MixResult:
    """Data class to hold the result of image mixing operation."""
    
    def __init__(self, mixed_image: np.ndarray, mixed_bg_image: np.ndarray, 
                 blend_params: Dict[str, Any]):
        """
        Initialize a MixResult.
        
        Args:
            mixed_image: The result of mixing facial regions
            mixed_bg_image: The result of mixing with background regions
            blend_params: Parameters used for blending
        """
        self.mixed_image = mixed_image
        self.mixed_bg_image = mixed_bg_image
        self.blend_params = blend_params


class ImageMixer:
    """
    Handles mixing and blending of facial regions between images.
    """
    
    def __init__(self, mask_generator: MaskGenerator):
        """
        Initialize the ImageMixer.
        
        Args:
            mask_generator: MaskGenerator instance for creating masks
        """
        self.mask_generator = mask_generator
    
    def calculate_scale_factors(self, source_region: Tuple[int, int, int], 
                              target_region: Tuple[int, int, int]) -> Tuple[float, float]:
        """
        Calculate scaling factors to match source region to target region.
        
        Args:
            source_region: Source region parameters (center, axis_h, axis_v)
            target_region: Target region parameters (center, axis_h, axis_v)
            
        Returns:
            Tuple of (horizontal_scale, vertical_scale)
        """
        _, source_h, source_v = source_region
        _, target_h, target_v = target_region
        
        h_scale = target_h / source_h if source_h > 0 else 1.0
        v_scale = target_v / source_v if source_v > 0 else 1.0
        
        return h_scale, v_scale
    
    def scale_image_and_mask(self, image: np.ndarray, mask: np.ndarray, 
                           h_scale: float, v_scale: float) -> Tuple[np.ndarray, np.ndarray]:
        """
        Scale both image and mask by given factors.
        
        Args:
            image: Source image
            mask: Source mask
            h_scale: Horizontal scaling factor
            v_scale: Vertical scaling factor
            
        Returns:
            Tuple of (scaled_image, scaled_mask)
        """
        scaled_image = cv2.resize(image, None, fx=h_scale, fy=v_scale, 
                                interpolation=cv2.INTER_NEAREST)
        scaled_mask = cv2.resize(mask, None, fx=h_scale, fy=v_scale, 
                               interpolation=cv2.INTER_NEAREST)
        
        return scaled_image, scaled_mask
    
    def blend_regions(self, source_roi: np.ndarray, target_roi: np.ndarray, 
                     mask_roi: np.ndarray, blur_kernel_size: int) -> np.ndarray:
        """
        Blend source and target regions using the mask.
        
        Args:
            source_roi: Source region of interest
            target_roi: Target region of interest
            mask_roi: Mask for blending
            blur_kernel_size: Size of blur kernel for smooth blending
            
        Returns:
            Blended region
        """
        # Create blurred mask for smooth blending
        mask_blurred = ImageUtils.create_blurred_mask(mask_roi, blur_kernel_size)
        
        # Perform alpha blending
        blended_roi = source_roi * mask_blurred + target_roi * (1 - mask_blurred)
        
        return blended_roi.astype(np.uint8)
    
    def process_region_mixing(self, region_index: int, source_region: Tuple[int, int, int], 
                            target_region: Tuple[int, int, int], source_image: np.ndarray, 
                            source_mask: np.ndarray, target_image: np.ndarray, 
                            target_mask: np.ndarray, blur_kernel_size: int) -> np.ndarray:
        """
        Process mixing of a specific facial region.
        
        Args:
            region_index: Index of the region in contours (0=mouth, 1=right_eye, 2=left_eye)
            source_region: Source region parameters (center, axis_h, axis_v)
            target_region: Target region parameters (center, axis_h, axis_v)
            source_image: Source image
            source_mask: Source mask
            target_image: Target image to mix into
            target_mask: Target mask
            blur_kernel_size: Blur kernel size for blending
            
        Returns:
            Updated target image with mixed region
        """
        try:
            # Calculate scaling factors (target/source)
            h_scale, v_scale = self.calculate_scale_factors(source_region, target_region)
            
            # Scale source image and mask to match target region size
            scaled_source, scaled_mask = self.scale_image_and_mask(
                source_image.copy(), source_mask.copy(), h_scale, v_scale
            )
            
            # Find contours
            source_contours, _ = cv2.findContours(scaled_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            target_contours, _ = cv2.findContours(target_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            if len(source_contours) <= region_index or len(target_contours) <= region_index:
                return target_image
            
            # Convert target mask to BGR for processing - Following notebook exactly
            target_mask_bgr = cv2.cvtColor(target_mask, cv2.COLOR_GRAY2BGR)
            
            # Get bounding rectangles - Following notebook convention: y, x, h, w = cv2.boundingRect
            y_src, x_src, h_src, w_src = cv2.boundingRect(source_contours[region_index])
            y_tgt, x_tgt, h_tgt, w_tgt = cv2.boundingRect(target_contours[region_index])
            
            # Extract ROI following notebook exactly: roi = imageSc[x:x+wT, y:y+hT, :]
            # This gives shape (wT, hT, 3)
            source_roi = scaled_source[x_src:x_src+w_tgt, y_src:y_src+h_tgt, :]
            
            # Extract target ROI and mask ROI - Following notebook exactly
            # maskRoi = maskT[xT:xT+wT, yT:yT+hT,:]
            # target_subsection = mixImage[xT:xT+wT, yT:yT+hT, :]
            target_roi = target_image[x_tgt:x_tgt+w_tgt, y_tgt:y_tgt+h_tgt, :]
            mask_roi = target_mask_bgr[x_tgt:x_tgt+w_tgt, y_tgt:y_tgt+h_tgt, :]
            
            # Check if ROIs are valid (notebook doesn't do this but we should)
            if source_roi.size == 0 or target_roi.size == 0 or mask_roi.size == 0:
                return target_image
            
            # Ensure dimensions match by taking minimum (safety check)
            min_shape_0 = min(source_roi.shape[0], target_roi.shape[0], mask_roi.shape[0])
            min_shape_1 = min(source_roi.shape[1], target_roi.shape[1], mask_roi.shape[1])
            
            if min_shape_0 <= 0 or min_shape_1 <= 0:
                return target_image
                
            source_roi = source_roi[:min_shape_0, :min_shape_1, :]
            target_roi = target_roi[:min_shape_0, :min_shape_1, :]
            mask_roi = mask_roi[:min_shape_0, :min_shape_1, :]
            
            # Create blurred mask for smooth blending - Following notebook exactly
            mask_blur = cv2.GaussianBlur(mask_roi, (blur_kernel_size, blur_kernel_size), 0)
            blended_mask = mask_blur + mask_roi
            blended_mask = blended_mask.astype(np.float32) / 255.0
            
            # Perform alpha blending - Following notebook exactly  
            blended_roi = source_roi * blended_mask + target_roi * (1 - blended_mask)
            blended_roi = blended_roi.astype(np.uint8)
            
            # Update target image - Following notebook exactly
            # mixImage[xT:xT+wT, yT:yT+hT, :] = blended_roi
            target_image[x_tgt:x_tgt+min_shape_0, y_tgt:y_tgt+min_shape_1, :] = blended_roi
            
            return target_image
            
        except Exception as e:
            print(f"Error in region mixing: {e}")
            return target_image
    
    def process_background_region(self, region_index: int, background_image: np.ndarray, 
                                target_image: np.ndarray, target_mask: np.ndarray, 
                                blur_kernel_size: int) -> np.ndarray:
        """
        Process mixing with background region (for creating background versions).
        
        Args:
            region_index: Index of the region in contours
            background_image: Background image to sample from
            target_image: Target image to mix into
            target_mask: Target mask
            blur_kernel_size: Blur kernel size for blending
            
        Returns:
            Updated target image with background region
        """
        try:
            # Random scaling for background
            scale_random = random.uniform(0.95, 1.05)
            scaled_bg = cv2.resize(background_image, None, fx=scale_random, fy=scale_random, 
                                 interpolation=cv2.INTER_NEAREST)
            
            # Find contours
            target_contours, _ = cv2.findContours(target_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            if len(target_contours) <= region_index:
                return target_image
            
            # Get target bounding rectangle - Following notebook convention: y, x, h, w
            y_tgt, x_tgt, h_tgt, w_tgt = cv2.boundingRect(target_contours[region_index])
            
            # Check if scaled background is large enough, if not, scale more
            # Following notebook: if(imageSc.shape[1]<(1.2*hT)) or (imageSc.shape[0]<(1.2*wT))
            if (scaled_bg.shape[1] < (1.2 * h_tgt)) or (scaled_bg.shape[0] < (1.2 * w_tgt)):
                scale_random = 1.3
                scaled_bg = cv2.resize(background_image, None, fx=scale_random, fy=scale_random, 
                                     interpolation=cv2.INTER_NEAREST)
            
            # Random position in background image, ensuring we don't go out of bounds
            # Following notebook: y, x, =  (random.randint(0, imageSc.shape[1]-hT), random.randint(0, imageSc.shape[0]-wT))
            max_y = max(0, scaled_bg.shape[1] - h_tgt)
            max_x = max(0, scaled_bg.shape[0] - w_tgt)
            y_bg = random.randint(0, max_y) if max_y > 0 else 0
            x_bg = random.randint(0, max_x) if max_x > 0 else 0
            
            # Extract background ROI - Following notebook exactly
            # roi = imageSc[x:x+wT, y:y+hT, :]
            bg_roi = scaled_bg[x_bg:x_bg+w_tgt, y_bg:y_bg+h_tgt, :]
            
            # Extract target ROI and mask ROI - Following notebook exactly
            # maskRoi = maskT[xT:xT+wT, yT:yT+hT,:]
            # target_subsection = mixImage[xT:xT+wT, yT:yT+hT, :]
            target_mask_bgr = cv2.cvtColor(target_mask, cv2.COLOR_GRAY2BGR)
            target_roi = target_image[x_tgt:x_tgt+w_tgt, y_tgt:y_tgt+h_tgt, :]
            mask_roi = target_mask_bgr[x_tgt:x_tgt+w_tgt, y_tgt:y_tgt+h_tgt, :]
            
            # Ensure all ROIs have matching dimensions
            min_h = min(bg_roi.shape[0], target_roi.shape[0], mask_roi.shape[0])
            min_w = min(bg_roi.shape[1], target_roi.shape[1], mask_roi.shape[1])
            
            if min_h <= 0 or min_w <= 0:
                return target_image
                
            bg_roi = bg_roi[:min_h, :min_w, :]
            target_roi = target_roi[:min_h, :min_w, :]
            mask_roi = mask_roi[:min_h, :min_w, :]
            
            # Create blurred mask for smooth blending
            mask_blur = cv2.GaussianBlur(mask_roi, (blur_kernel_size, blur_kernel_size), 0)
            blended_mask = mask_blur + mask_roi
            blended_mask = blended_mask.astype(np.float32) / 255.0
            
            # Perform alpha blending
            blended_roi = bg_roi * blended_mask + target_roi * (1 - blended_mask)
            blended_roi = blended_roi.astype(np.uint8)
            
            # Update target image - Following notebook exactly
            # mixImage[xT:xT+wT, yT:yT+hT, :] = blended_roi
            target_image[x_tgt:x_tgt+min_w, y_tgt:y_tgt+min_h, :] = blended_roi
            
            return target_image
            
        except Exception as e:
            print(f"Error in background region mixing: {e}")
            return target_image
    
    def mix_images(self, source_data: Dict[str, Any], target_data: Dict[str, Any], 
                  background_image: Optional[np.ndarray] = None, 
                  mix_eyes: bool = True, mix_mouth: bool = True,
                  blur_range: Tuple[int, int] = (5, 7)) -> MixResult:
        """
        Mix facial regions between source and target images.
        
        Args:
            source_data: Source image mask data from MaskGenerator
            target_data: Target image mask data from MaskGenerator
            background_image: Optional background image for background mixing
            mix_eyes: Whether to mix eye regions
            mix_mouth: Whether to mix mouth region
            blur_range: Range for random blur kernel size
            
        Returns:
            MixResult containing mixed images and parameters
        """
        # Extract data
        source_image = source_data['original_image']
        source_mask = source_data['combined_mask']
        source_regions = self.mask_generator.get_region_parameters(source_data)
        
        target_image = target_data['original_image']
        target_mask = target_data['combined_mask']
        target_regions = self.mask_generator.get_region_parameters(target_data)
        
        # Initialize result images
        mixed_image = target_image.copy()
        mixed_bg_image = target_image.copy() if background_image is not None else None
        
        # Generate random blur parameter
        blur_param = random.randint(*blur_range)
        if blur_param % 2 == 0:
            blur_param += 1
        
        blend_params = {'blur_kernel_size': blur_param}
        
        # Mix regions if requested
        if mix_eyes:
            # Mix left eye (region index 2)
            if 'left_eye' in source_regions and 'left_eye' in target_regions:
                mixed_image = self.process_region_mixing(
                    2, source_regions['left_eye'], target_regions['left_eye'],
                    source_image, source_mask, mixed_image, target_mask, blur_param
                )
                
                if mixed_bg_image is not None:
                    mixed_bg_image = self.process_background_region(
                        2, background_image, mixed_bg_image, target_mask, blur_param
                    )
            
            # Mix right eye (region index 1)
            if 'right_eye' in source_regions and 'right_eye' in target_regions:
                mixed_image = self.process_region_mixing(
                    1, source_regions['right_eye'], target_regions['right_eye'],
                    source_image, source_mask, mixed_image, target_mask, blur_param
                )
                
                if mixed_bg_image is not None:
                    mixed_bg_image = self.process_background_region(
                        1, background_image, mixed_bg_image, target_mask, blur_param
                    )
        
        if mix_mouth:
            # Mix mouth (region index 0)
            if 'mouth' in source_regions and 'mouth' in target_regions:
                mixed_image = self.process_region_mixing(
                    0, source_regions['mouth'], target_regions['mouth'],
                    source_image, source_mask, mixed_image, target_mask, blur_param
                )
                
                if mixed_bg_image is not None:
                    mixed_bg_image = self.process_background_region(
                        0, background_image, mixed_bg_image, target_mask, blur_param
                    )
        
        return MixResult(mixed_image, mixed_bg_image, blend_params)
    
    def save_mixed_images(self, mix_result: MixResult, output_dir: str, 
                         base_filename: str) -> Dict[str, str]:
        """
        Save mixed images to files.
        
        Args:
            mix_result: MixResult from mix_images
            output_dir: Directory to save images
            base_filename: Base filename for output files
            
        Returns:
            Dictionary mapping image types to saved file paths
        """
        import os
        
        saved_files = {}
        
        # Save mixed image
        mixed_path = os.path.join(output_dir, f"{base_filename}_mixed.png")
        cv2.imwrite(mixed_path, mix_result.mixed_image)
        saved_files['mixed'] = mixed_path
        
        # Save background mixed image if available
        if mix_result.mixed_bg_image is not None:
            bg_path = os.path.join(output_dir, f"{base_filename}_mixed_bg.png")
            cv2.imwrite(bg_path, mix_result.mixed_bg_image)
            saved_files['mixed_bg'] = bg_path
        
        return saved_files
