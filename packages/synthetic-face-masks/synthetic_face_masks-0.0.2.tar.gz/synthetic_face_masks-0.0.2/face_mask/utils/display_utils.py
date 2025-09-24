"""
Display and visualization utilities for the Face Mixing Dataset Generator.

This module contains helper functions for visualization, directory exploration,
and image display tasks used throughout the face_mask project.

Located in face_mask.utils.display_utils for organized project structure.
"""

import os
import glob
import matplotlib.pyplot as plt
from PIL import Image


def display_sample_images(directory, title, max_images=6):
    """
    Display sample images from a directory in a grid layout.
    
    Args:
        directory (str): Path to the directory containing images
        title (str): Title for the visualization
        max_images (int): Maximum number of images to display (default: 6)
    """
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return
    
    # Get image files
    image_files = glob.glob(os.path.join(directory, "*.jpg")) + \
                  glob.glob(os.path.join(directory, "*.png"))
    
    if not image_files:
        print(f"No images found in {directory}")
        return
    
    # Limit number of images
    image_files = image_files[:max_images]
    
    # Calculate grid size
    n_images = len(image_files)
    cols = min(3, n_images)
    rows = (n_images + cols - 1) // cols
    
    # Create subplot
    fig, axes = plt.subplots(rows, cols, figsize=(15, 5*rows))
    fig.suptitle(f"{title} (Showing {n_images} images)", fontsize=16)
    
    # Handle single image case
    if n_images == 1:
        axes = [axes]
    elif rows == 1:
        axes = axes if hasattr(axes, '__iter__') else [axes]
    else:
        axes = axes.flatten()
    
    # Display images
    for i, img_path in enumerate(image_files):
        try:
            img = Image.open(img_path)
            axes[i].imshow(img)
            axes[i].set_title(os.path.basename(img_path), fontsize=10)
            axes[i].axis('off')
        except Exception as e:
            axes[i].text(0.5, 0.5, f'Error loading\n{os.path.basename(img_path)}', 
                        ha='center', va='center', transform=axes[i].transAxes)
            axes[i].axis('off')
    
    # Hide unused subplots
    for i in range(n_images, len(axes)):
        axes[i].axis('off')
    
    plt.tight_layout()
    plt.show()




def count_images_in_subfolders(base_path):
    """
    Count images in all subfolders of a given path.
    
    Args:
        base_path (str): Path to the base directory
        
    Returns:
        dict: Dictionary mapping subfolder names to image counts
    """
    subfolder_stats = {}
    
    if not os.path.exists(base_path):
        return subfolder_stats
    
    subfolders = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    
    for subfolder in subfolders:
        folder_path = os.path.join(base_path, subfolder)
        image_files = [f for f in os.listdir(folder_path) 
                      if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        subfolder_stats[subfolder] = len(image_files)
    
    return subfolder_stats

def display_sample_from_subfolders(base_path, num_samples=3):
    """
    Display sample images from all subfolders on the same axes.
    
    Args:
        base_path (str): Path to the base directory containing subfolders
        num_samples (int): Total number of sample images to display from all folders (default: 3)
    """
    if not os.path.exists(base_path):
        print(f"Directory not found: {base_path}")
        return
    
    subfolders = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    
    if not subfolders:
        print("No subfolders found")
        return
    
    print(f"Found {len(subfolders)} subfolders: {subfolders}")
    
    # Collect all image files from all subfolders
    all_images = []
    for subfolder in subfolders:
        folder_path = os.path.join(base_path, subfolder)
        image_files = [f for f in os.listdir(folder_path) 
                      if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        for image_file in image_files:
            all_images.append((subfolder, os.path.join(folder_path, image_file), image_file))
    
    if not all_images:
        print("No images found in any subfolder")
        return
    
    # Limit to num_samples total images
    selected_images = all_images[:num_samples]
    num_to_show = len(selected_images)
    
    # Calculate grid layout
    cols = min(3, num_to_show)
    rows = (num_to_show + cols - 1) // cols
    
    # Create single plot with all images
    fig, axes = plt.subplots(rows, cols, figsize=(4*cols, 4*rows))
    
    # Handle single image case
    if num_to_show == 1:
        axes = [axes]
    elif rows == 1:
        axes = axes if hasattr(axes, '__iter__') else [axes]
    else:
        axes = axes.flatten()
    
    # Display images
    for i, (subfolder, img_path, img_filename) in enumerate(selected_images):
        try:
            img = Image.open(img_path)
            axes[i].imshow(img)
            axes[i].set_title(f"{subfolder}/{img_filename}")
            axes[i].axis('off')
        except Exception as e:
            axes[i].text(0.5, 0.5, f'Error loading', ha='center', va='center')
            axes[i].axis('off')
    
    # Hide unused subplots
    for i in range(num_to_show, len(axes)):
        axes[i].axis('off')
    
    plt.suptitle(f"Sample Images from All Subfolders (Showing {num_to_show} of {len(all_images)} total)", fontsize=14)
    plt.tight_layout()
    plt.show()


