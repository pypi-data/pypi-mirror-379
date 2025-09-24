#!/usr/bin/env python3
"""
Basic example of using the Face Mixing Dataset Generator.

This example demonstrates:
1. Setting up a basic configuration
2. Processing a folder of face images
3. Generating mixed images with default settings
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from face_mask.core.dataset_generator import DatasetGenerator, DatasetConfig


def basic_example():
    """Run a basic dataset generation example."""
    
    # Configuration
    input_folder = "./testImages"  # Adjust path as needed
    output_folder = "./basic_output"
    
    # Create configuration
    config = DatasetConfig(
        input_folder=input_folder,
        output_folder=output_folder,
        mix_probability=0.5,  # 50% chance of creating mixed images
        ellipse_probability=0.5,  # 50% chance of ellipse vs rectangle masks
        train_split_ratio=0.8  # 80% for training, 20% for testing
    )
    
    print("Basic Face Mixing Example")
    print("=" * 30)
    print(f"Input folder: {config.input_folder}")
    print(f"Output folder: {config.output_folder}")
    print(f"Mix probability: {config.mix_probability}")
    print()
    
    try:
        # Initialize generator
        generator = DatasetGenerator(config)
        
        # Generate dataset
        print("Starting dataset generation...")
        stats = generator.generate_dataset()
        
        # Print results
        print("\nGeneration Complete!")
        print(f"Total images: {stats['total_images']}")
        print(f"Normal images: {stats['normal_images']}")
        print(f"Mixed images: {stats['mixed_images']}")
        print(f"Failed images: {stats['failed_images']}")
        
        # Validate dataset
        print("\nValidating dataset...")
        validation = generator.validate_dataset()
        if validation.get('valid', False):
            print("✓ Dataset is valid")
            print(f"  Images: {validation['num_images']}")
            print(f"  Annotations: {validation['num_annotations']}")
        else:
            print("✗ Dataset validation failed")
            print(f"  Error: {validation.get('error', 'Unknown error')}")
        
        # Generate report
        print("\nGenerating report...")
        generator.generate_report()
        print("Report saved to dataset_report.json")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    basic_example()
