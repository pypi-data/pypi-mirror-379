#!/usr/bin/env python3
"""
Face Mixing Dataset Generator - Main Entry Point

This script provides a command-line interface for generating face mixing datasets.
It processes face images to create synthetic training data with mixed facial regions.

Usage:
    python main.py --input_folder /path/to/faces --output_folder /path/to/output
    
For more options, run:
    python main.py --help
"""

import argparse
import os
import sys
import json
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from face_mask.core.dataset_generator import DatasetGenerator, DatasetConfig


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate face mixing datasets for computer vision training",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Required arguments
    parser.add_argument(
        "--input_folder", "-i",
        type=str,
        required=True,
        help="Path to folder containing face images"
    )
    
    parser.add_argument(
        "--output_folder", "-o",
        type=str,
        required=True,
        help="Path to output folder for generated dataset"
    )
    
    # Optional arguments
    parser.add_argument(
        "--background_folder", "-b",
        type=str,
        default=None,
        help="Path to folder containing background images (optional)"
    )
    
    parser.add_argument(
        "--crop_border",
        type=int,
        default=50,
        help="Number of pixels to crop from image borders"
    )
    
    parser.add_argument(
        "--target_width",
        type=int,
        default=320,
        help="Target width for processed images"
    )
    
    parser.add_argument(
        "--target_height",
        type=int,
        default=320,
        help="Target height for processed images"
    )
    
    parser.add_argument(
        "--mix_probability",
        type=float,
        default=0.5,
        help="Probability of creating mixed images vs normal images (0.0-1.0)"
    )
    
    parser.add_argument(
        "--ellipse_probability",
        type=float,
        default=0.5,
        help="Probability of using ellipse vs rectangle masks (0.0-1.0)"
    )
    
    parser.add_argument(
        "--train_split_ratio",
        type=float,
        default=0.8,
        help="Ratio of images for training set (0.0-1.0)"
    )
    
    parser.add_argument(
        "--config_file",
        type=str,
        default=None,
        help="Path to JSON configuration file (overrides command line args)"
    )
    
    parser.add_argument(
        "--validate_only",
        action="store_true",
        help="Only validate existing dataset without generating new images"
    )
    
    parser.add_argument(
        "--generate_report",
        action="store_true",
        help="Generate dataset analysis report"
    )
    
    return parser.parse_args()


def load_config_from_file(config_file: str) -> dict:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading config file {config_file}: {e}")
        return {}


def create_config_from_args(args) -> DatasetConfig:
    """Create DatasetConfig from command line arguments."""
    
    # Load from config file if provided
    config_dict = {}
    if args.config_file and os.path.exists(args.config_file):
        config_dict = load_config_from_file(args.config_file)
        print(f"Loaded configuration from: {args.config_file}")
    
    # Override with command line arguments
    config_params = {
        'input_folder': args.input_folder,
        'output_folder': args.output_folder,
        'background_folder': args.background_folder,
        'crop_border': args.crop_border,
        'target_size': (args.target_width, args.target_height),
        'mix_probability': args.mix_probability,
        'ellipse_probability': args.ellipse_probability,
        'train_split_ratio': args.train_split_ratio
    }
    
    # Update with config file values, but command line takes precedence
    for key, value in config_dict.items():
        if key in config_params and value is not None:
            if key != 'target_size':  # Handle target_size specially
                config_params[key] = value
            else:
                config_params[key] = tuple(value)
    
    return DatasetConfig(**config_params)


def validate_config(config: DatasetConfig) -> bool:
    """Validate configuration parameters."""
    errors = []
    
    # Check input folder exists
    if not os.path.exists(config.input_folder):
        errors.append(f"Input folder does not exist: {config.input_folder}")
    
    # Check background folder if specified
    if config.background_folder and not os.path.exists(config.background_folder):
        errors.append(f"Background folder does not exist: {config.background_folder}")
    
    # Check probability ranges
    if not 0.0 <= config.mix_probability <= 1.0:
        errors.append("mix_probability must be between 0.0 and 1.0")
    
    if not 0.0 <= config.ellipse_probability <= 1.0:
        errors.append("ellipse_probability must be between 0.0 and 1.0")
    
    if not 0.0 <= config.train_split_ratio <= 1.0:
        errors.append("train_split_ratio must be between 0.0 and 1.0")
    
    # Check target size
    if config.target_size[0] <= 0 or config.target_size[1] <= 0:
        errors.append("target_size dimensions must be positive")
    
    if errors:
        print("Configuration errors:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    return True


def print_config_summary(config: DatasetConfig):
    """Print configuration summary."""
    print("\nDataset Generation Configuration:")
    print(f"  Input folder: {config.input_folder}")
    print(f"  Output folder: {config.output_folder}")
    print(f"  Background folder: {config.background_folder or 'None'}")
    print(f"  Target size: {config.target_size[0]}x{config.target_size[1]}")
    print(f"  Crop border: {config.crop_border} pixels")
    print(f"  Mix probability: {config.mix_probability:.2f}")
    print(f"  Ellipse probability: {config.ellipse_probability:.2f}")
    print(f"  Train split ratio: {config.train_split_ratio:.2f}")
    print()


def save_generation_config(config: DatasetConfig, output_folder: str):
    """Save the generation configuration to the output folder."""
    config_dict = {
        'input_folder': config.input_folder,
        'output_folder': config.output_folder,
        'background_folder': config.background_folder,
        'crop_border': config.crop_border,
        'target_size': list(config.target_size),
        'mix_probability': config.mix_probability,
        'ellipse_probability': config.ellipse_probability,
        'train_split_ratio': config.train_split_ratio
    }
    
    config_path = os.path.join(output_folder, "generation_config.json")
    with open(config_path, 'w') as f:
        json.dump(config_dict, f, indent=4)
    
    print(f"Generation configuration saved to: {config_path}")


def main():
    """Main function."""
    print("Face Mixing Dataset Generator")
    print("=" * 40)
    
    # Parse arguments
    args = parse_arguments()
    
    # Create configuration
    config = create_config_from_args(args)
    
    # Validate configuration
    if not validate_config(config):
        sys.exit(1)
    
    # Print configuration summary
    print_config_summary(config)
    
    try:
        # Initialize dataset generator
        generator = DatasetGenerator(config)
        
        if args.validate_only:
            # Only validate existing dataset
            print("Validating existing dataset...")
            validation_result = generator.validate_dataset()
            print(f"Validation result: {validation_result}")
            
        elif args.generate_report:
            # Generate analysis report
            print("Generating dataset report...")
            generator.generate_report()
            print("Report generated successfully")
            
        else:
            # Generate dataset
            print("Starting dataset generation...")
            stats = generator.generate_dataset()
            
            # Print generation statistics
            print("\nDataset Generation Complete!")
            print(f"  Total images generated: {stats['total_images']}")
            print(f"  Normal images: {stats['normal_images']}")
            print(f"  Mixed images: {stats['mixed_images']}")
            print(f"  Failed images: {stats['failed_images']}")
            print(f"  Output saved to: {stats['output_folder']}")
            
            # Save generation config
            save_generation_config(config, config.output_folder)
            
            # Validate generated dataset
            print("\nValidating generated dataset...")
            validation_result = generator.validate_dataset()
            if validation_result.get('valid', False):
                print("✓ Dataset validation successful")
            else:
                print(f"✗ Dataset validation failed: {validation_result.get('error', 'Unknown error')}")
            
            # Generate report
            print("Generating dataset report...")
            generator.generate_report()
            
    except KeyboardInterrupt:
        print("\nDataset generation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nError during dataset generation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
