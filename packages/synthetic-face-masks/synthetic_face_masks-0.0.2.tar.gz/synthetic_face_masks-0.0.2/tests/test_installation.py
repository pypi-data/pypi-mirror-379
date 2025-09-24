#!/usr/bin/env python3
"""
Simple test script to verify the face mixing project installation and basic functionality.
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    try:
        from face_mask.core.face_processor import FaceProcessor
        print("✓ FaceProcessor import successful")
        
        from face_mask.core.mask_generator import MaskGenerator
        print("✓ MaskGenerator import successful")
        
        from face_mask.core.image_mixer import ImageMixer
        print("✓ ImageMixer import successful")
        
        from face_mask.core.dataset_generator import DatasetGenerator, DatasetConfig
        print("✓ DatasetGenerator import successful")
        
        from face_mask.utils.image_utils import ImageUtils
        print("✓ ImageUtils import successful")
        
        from face_mask.utils.coco_utils import COCOUtils
        print("✓ COCOUtils import successful")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False


def test_basic_functionality():
    """Test basic functionality without requiring image files."""
    print("\nTesting basic functionality...")
    
    try:
        # Test FaceProcessor initialization
        from face_mask.core.face_processor import FaceProcessor
        face_processor = FaceProcessor()
        print("✓ FaceProcessor initialization successful")
        
        # Test MaskGenerator initialization
        from face_mask.core.mask_generator import MaskGenerator
        mask_generator = MaskGenerator(face_processor)
        print("✓ MaskGenerator initialization successful")
        
        # Test ImageMixer initialization
        from face_mask.core.image_mixer import ImageMixer
        image_mixer = ImageMixer(mask_generator)
        print("✓ ImageMixer initialization successful")
        
        # Test COCOUtils
        from face_mask.utils.coco_utils import COCOUtils
        coco_utils = COCOUtils()
        img_ann, obj_ann = coco_utils.generate_coco_annotations("test.jpg", 1, 1)
        print("✓ COCOUtils functionality successful")
        
        # Test ImageUtils
        from face_mask.utils.image_utils import ImageUtils
        distance = ImageUtils.get_distance((0, 0), (3, 4))
        assert distance == 2  # sqrt(9+16)/2 = 5/2 = 2.5 -> int(2.5) = 2
        print("✓ ImageUtils functionality successful")
        
        return True
        
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_dependencies():
    """Test that required dependencies are available."""
    print("\nTesting dependencies...")
    
    dependencies = [
        "cv2",
        "mediapipe", 
        "numpy",
        "imgaug",
        "tqdm"
    ]
    
    missing_deps = []
    
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✓ {dep} available")
        except ImportError:
            print(f"✗ {dep} not available")
            missing_deps.append(dep)
    
    if missing_deps:
        print(f"\nMissing dependencies: {', '.join(missing_deps)}")
        print("Install with: pip install -r requirements.txt")
        return False
    
    return True


def test_configuration():
    """Test configuration management."""
    print("\nTesting configuration management...")
    
    try:
        from face_mask.core.dataset_generator import DatasetConfig
        
        # Test DatasetConfig creation
        dataset_config = DatasetConfig(
            input_folder="/test/input",
            output_folder="/test/output"
        )
        print("✓ DatasetConfig creation successful")
        
        print("✓ Configuration working")
        
        return True
        
    except Exception as e:
        print(f"✗ Configuration test failed: {e}")
        return False


def main():
    """Run all tests."""
    print("Face Mixing Project - Installation Test")
    print("=" * 45)
    
    tests = [
        ("Import Test", test_imports),
        ("Dependencies Test", test_dependencies),
        ("Basic Functionality Test", test_basic_functionality),
        ("Configuration Test", test_configuration),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{test_name}")
        print("-" * len(test_name))
        result = test_func()
        results.append((test_name, result))
    
    # Summary
    print("\n" + "=" * 45)
    print("TEST SUMMARY")
    print("=" * 45)
    
    all_passed = True
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 45)
    if all_passed:
        print("🎉 ALL TESTS PASSED! The installation is working correctly.")
        print("\nYou can now use the face mixing project:")
        print("  python main.py --help")
        print("  python examples/basic_example.py")
    else:
        print("❌ Some tests failed. Please check the error messages above.")
        print("\nCommon solutions:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Check Python version (3.7+ required)")
        print("  3. Verify MediaPipe installation")
    
    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
