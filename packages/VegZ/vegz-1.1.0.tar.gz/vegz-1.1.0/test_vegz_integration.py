#!/usr/bin/env python3
"""
Test VegZ integration to ensure the enhanced error detection works with the main package.
"""

import sys
import os
import pandas as pd

# Copyright (c) 2025 Mohamed Z. Hatim
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Copyright (c) 2025 Mohamed Z. Hatim
try:
    from VegZ import VegZ
    from VegZ.data_management.standardization import SpeciesNameStandardizer, DataStandardizer
    print("[PASS] All imports successful")
except ImportError as e:
    print(f"[FAIL] Import error: {e}")
    sys.exit(1)

def test_vegz_main_class():
    """Test the main VegZ class integration."""
    print("\n=== Testing VegZ Main Class Integration ===")

    # Copyright (c) 2025 Mohamed Z. Hatim
    veg = VegZ()
    print("[PASS] VegZ initialized successfully")

    # Copyright (c) 2025 Mohamed Z. Hatim
    test_data = pd.DataFrame({
        'species': ['Quercus alba', 'Pinus sp.', 'quercus ALBA', 'Acer saccharum L.'],
        'abundance': [25, 15, 10, 30]
    })

    # Copyright (c) 2025 Mohamed Z. Hatim
    try:
        standardizer = veg.species_standardizer if hasattr(veg, 'species_standardizer') else SpeciesNameStandardizer()

        # Copyright (c) 2025 Mohamed Z. Hatim
        result = standardizer.validate_species_name('Quercus alba')
        assert 'is_valid' in result
        assert 'errors' in result
        assert 'suggestions' in result
        print("[PASS] Error detection functionality accessible")

        # Copyright (c) 2025 Mohamed Z. Hatim
        name_type = standardizer.classify_name_type('Quercus alba')
        assert name_type == 'binomial'
        print("[PASS] Name classification working")

        # Copyright (c) 2025 Mohamed Z. Hatim
        batch_results = standardizer.batch_validate_names(['Quercus alba', 'Pinus sp.'])
        assert len(batch_results) == 2
        print("[PASS] Batch validation working")

    except Exception as e:
        print(f"[FAIL] Error in enhanced functionality: {e}")
        return False

    return True

def test_data_standardizer_integration():
    """Test the DataStandardizer class with enhanced features."""
    print("\n=== Testing DataStandardizer Integration ===")

    try:
        # Copyright (c) 2025 Mohamed Z. Hatim
        standardizer = DataStandardizer()
        print("[PASS] DataStandardizer initialized")

        # Copyright (c) 2025 Mohamed Z. Hatim
        assert hasattr(standardizer, 'species_standardizer')
        assert hasattr(standardizer.species_standardizer, 'validate_species_name')
        print("[PASS] Enhanced SpeciesNameStandardizer integrated")

        # Copyright (c) 2025 Mohamed Z. Hatim
        test_df = pd.DataFrame({
            'species': ['Quercus alba', 'Pinus sp.', 'ACER SACCHARUM'],
            'latitude': [45.5, 46.1, 44.8],
            'longitude': [-73.6, -74.2, -72.9]
        })

        # Copyright (c) 2025 Mohamed Z. Hatim
        result_df = standardizer.species_standardizer.standardize_dataframe(
            test_df,
            include_error_detection=True
        )

        # Copyright (c) 2025 Mohamed Z. Hatim
        error_columns = [col for col in result_df.columns if col.startswith('name_')]
        assert len(error_columns) > 0
        print(f"[PASS] Error detection columns added: {len(error_columns)}")

        # Copyright (c) 2025 Mohamed Z. Hatim
        simple_df = standardizer.species_standardizer.standardize_dataframe(
            test_df,
            include_error_detection=False
        )

        # Copyright (c) 2025 Mohamed Z. Hatim
        expected_cols = ['species_original', 'genus', 'specific_epithet']
        assert all(col in simple_df.columns for col in expected_cols)
        print("[PASS] Backward compatibility maintained")

    except Exception as e:
        print(f"[FAIL] DataStandardizer integration error: {e}")
        return False

    return True

def test_comprehensive_functionality():
    """Test comprehensive functionality end-to-end."""
    print("\n=== Testing Comprehensive Functionality ===")

    try:
        standardizer = SpeciesNameStandardizer()

        # Copyright (c) 2025 Mohamed Z. Hatim
        test_cases = {
            'valid_binomial': ('Quercus alba', True),
            'genus_only': ('Quercus', False),
            'author_citation': ('Quercus alba L.', False),
            'hybrid': ('Quercus × alba', False),
            'placeholder': ('Quercus sp.', False),
            'invalid_chars': ('Quercus alba!', False),
            'formatting': ('quercus alba', False),
        }

        for test_name, (species_name, expected_valid) in test_cases.items():
            result = standardizer.validate_species_name(species_name)
            actual_valid = result['is_valid']

            if actual_valid == expected_valid:
                print(f"[PASS] {test_name}: '{species_name}' -> Valid: {actual_valid}")
            else:
                print(f"[FAIL] {test_name}: '{species_name}' -> Expected: {expected_valid}, Got: {actual_valid}")
                return False

        # Copyright (c) 2025 Mohamed Z. Hatim
        test_df = pd.DataFrame({
            'species': list(test_cases.keys())  # Use the species names
        })

        # Copyright (c) 2025 Mohamed Z. Hatim
        test_df['species'] = [name for name, valid in test_cases.values()]

        report = standardizer.generate_error_report(test_df)

        assert 'summary' in report
        assert 'error_statistics' in report
        assert 'recommendations' in report
        print("[PASS] Error reporting functionality working")

    except Exception as e:
        print(f"[FAIL] Comprehensive functionality error: {e}")
        import traceback
        traceback.print_exc()
        return False

    return True

def main():
    """Run all integration tests."""
    print("VegZ Enhanced Error Detection - INTEGRATION TESTS")
    print("=" * 60)

    tests = [
        test_vegz_main_class,
        test_data_standardizer_integration,
        test_comprehensive_functionality
    ]

    passed = 0
    failed = 0

    for test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"[FAIL] {test_func.__name__} crashed: {e}")
            failed += 1

    print("\n" + "=" * 60)
    print("INTEGRATION TEST RESULTS")
    print("=" * 60)
    print(f"Tests passed: {passed}")
    print(f"Tests failed: {failed}")
    print(f"Total tests: {passed + failed}")

    if failed == 0:
        print("\n[PASS] ALL INTEGRATION TESTS PASSED!")
        print("\nThe enhanced error detection functionality has been successfully")
        print("integrated into the VegZ package and is fully functional.")
        return True
    else:
        print(f"\n[FAIL] {failed} integration tests failed.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)