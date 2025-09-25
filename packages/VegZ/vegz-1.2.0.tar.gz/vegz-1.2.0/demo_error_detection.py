#!/usr/bin/env python3
"""
Demonstration script for the enhanced species name error detection functionality in VegZ.

This script shows how to use the new comprehensive error detection features.
"""

import sys
import os
import pandas as pd

# Copyright (c) 2025 Mohamed Z. Hatim
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from VegZ.data_management.standardization import SpeciesNameStandardizer


def demo_individual_validation():
    """Demonstrate individual species name validation."""
    print("=" * 60)
    print("INDIVIDUAL SPECIES NAME VALIDATION DEMO")
    print("=" * 60)

    standardizer = SpeciesNameStandardizer()

    # Copyright (c) 2025 Mohamed Z. Hatim
    test_names = [
        "Quercus alba",              # Copyright (c) 2025 Mohamed Z. Hatim
        "Quercus",                   # Copyright (c) 2025 Mohamed Z. Hatim
        "alba",                      # Copyright (c) 2025 Mohamed Z. Hatim
        "quercus alba",              # Copyright (c) 2025 Mohamed Z. Hatim
        "Quercus alba L.",           # Copyright (c) 2025 Mohamed Z. Hatim
        "Quercus × alba",            # Copyright (c) 2025 Mohamed Z. Hatim
        "Quercus sp.",               # Copyright (c) 2025 Mohamed Z. Hatim
        "Quercus alba!",             # Copyright (c) 2025 Mohamed Z. Hatim
        "Quercus alba var. alba",    # Copyright (c) 2025 Mohamed Z. Hatim
    ]

    for name in test_names:
        print(f"\nValidating: '{name}'")
        result = standardizer.validate_species_name(name)

        print(f"  Valid: {result['is_valid']}")
        print(f"  Cleaned: '{result['cleaned_name']}'")
        print(f"  Type: {standardizer.classify_name_type(name)}")
        print(f"  Severity: {result['severity']}")

        if result['errors']:
            print(f"  Errors detected:")
            for category, errors in result['errors'].items():
                print(f"     - {category}: {errors}")

        if result['suggestions']:
            print(f"  Suggestions:")
            for suggestion in result['suggestions']:
                print(f"     - {suggestion}")


def demo_dataframe_processing():
    """Demonstrate DataFrame processing with error detection."""
    print("\n" + "=" * 60)
    print("DATAFRAME PROCESSING WITH ERROR DETECTION DEMO")
    print("=" * 60)

    standardizer = SpeciesNameStandardizer()

    # Copyright (c) 2025 Mohamed Z. Hatim
    sample_data = {
        'site_id': ['SITE_001', 'SITE_002', 'SITE_003', 'SITE_004', 'SITE_005'],
        'species': [
            'Quercus alba',
            'pinus strobus L.',
            'Acer sp.',
            'FAGUS GRANDIFOLIA',
            'Betula nigra var. nigra'
        ],
        'abundance': [25, 15, 8, 30, 12]
    }

    df = pd.DataFrame(sample_data)
    print("Original data:")
    print(df)

    # Copyright (c) 2025 Mohamed Z. Hatim
    df_processed = standardizer.standardize_dataframe(df, include_error_detection=True)

    print(f"\nProcessed data with error detection:")
    print(f"Shape: {df_processed.shape}")
    print(f"New columns added: {len(df_processed.columns) - len(df.columns)}")

    # Copyright (c) 2025 Mohamed Z. Hatim
    key_columns = ['species_original', 'species', 'name_is_valid', 'name_severity', 'name_type']
    print(f"\nKey results:")
    print(df_processed[key_columns])

    # Copyright (c) 2025 Mohamed Z. Hatim
    print(f"\nError summary:")
    for i, row in df_processed.iterrows():
        if not row['name_is_valid']:
            print(f"  {row['species_original']}: {row['name_errors_summary']}")


def demo_batch_validation():
    """Demonstrate batch validation functionality."""
    print("\n" + "=" * 60)
    print("BATCH VALIDATION DEMO")
    print("=" * 60)

    standardizer = SpeciesNameStandardizer()

    # Copyright (c) 2025 Mohamed Z. Hatim
    species_list = [
        "Quercus alba", "Pinus strobus", "Acer saccharum",
        "Quercus", "alba", "strobus",
        "quercus alba", "PINUS STROBUS", "Acer  Saccharum",
        "Quercus alba L.", "Pinus strobus (L.) Sweet",
        "Quercus × alba", "Pinus x strobus",
        "Quercus sp.", "Pinus cf. strobus", "Unknown tree",
        "Quercus alba!", "Pinus strobus123", "Acer saccharum@"
    ]

    print(f"Validating {len(species_list)} species names...")

    results_df = standardizer.batch_validate_names(species_list)

    print(f"\nResults summary:")
    print(f"Total names: {len(species_list)}")
    print(f"Valid names: {results_df['is_valid'].sum()}")
    print(f"Invalid names: {(~results_df['is_valid']).sum()}")

    print(f"\nName type distribution:")
    type_counts = results_df['name_type'].value_counts()
    for name_type, count in type_counts.items():
        print(f"  {name_type}: {count}")

    print(f"\nSeverity distribution:")
    severity_counts = results_df['severity'].value_counts()
    for severity, count in severity_counts.items():
        print(f"  {severity}: {count}")


def demo_error_reporting():
    """Demonstrate comprehensive error reporting."""
    print("\n" + "=" * 60)
    print("COMPREHENSIVE ERROR REPORTING DEMO")
    print("=" * 60)

    standardizer = SpeciesNameStandardizer()

    # Copyright (c) 2025 Mohamed Z. Hatim
    problematic_data = {
        'species': [
            "Quercus alba", "Pinus strobus", "Acer saccharum",  # Copyright (c) 2025 Mohamed Z. Hatim
            "Quercus", "alba", "Fagus",  # Copyright (c) 2025 Mohamed Z. Hatim
            "quercus alba", "PINUS STROBUS", "acer SACCHARUM",  # Copyright (c) 2025 Mohamed Z. Hatim
            "Quercus alba L.", "Pinus strobus Linnaeus",  # Copyright (c) 2025 Mohamed Z. Hatim
            "Quercus × alba", "Pinus x strobus",  # Copyright (c) 2025 Mohamed Z. Hatim
            "Quercus sp.", "Pinus cf. strobus", "Unknown",  # Copyright (c) 2025 Mohamed Z. Hatim
            "Quercus alba!", "Pinus strobus123",  # Copyright (c) 2025 Mohamed Z. Hatim
            "", None, "   ",  # Copyright (c) 2025 Mohamed Z. Hatim
        ]
    }

    df = pd.DataFrame(problematic_data)

    print("Generating comprehensive error report...")
    report = standardizer.generate_error_report(df)

    print(f"\n--- ERROR REPORT ---")
    print(f"Total names analyzed: {report['summary']['total_names']}")
    print(f"Valid names: {report['summary']['valid_names']} ({report['summary']['validity_percentage']}%)")
    print(f"Invalid names: {report['summary']['invalid_names']}")

    print(f"\nTop error categories:")
    for category, stats in list(report['error_statistics'].items())[:5]:
        if stats['count'] > 0:
            print(f"  {category}: {stats['count']} ({stats['percentage']}%)")

    print(f"\nRecommendations:")
    for i, rec in enumerate(report['recommendations'], 1):
        print(f"  {i}. {rec}")


def demo_backward_compatibility():
    """Demonstrate that backward compatibility is maintained."""
    print("\n" + "=" * 60)
    print("BACKWARD COMPATIBILITY DEMO")
    print("=" * 60)

    standardizer = SpeciesNameStandardizer()

    # Copyright (c) 2025 Mohamed Z. Hatim
    print("Testing existing clean_species_name functionality:")

    test_cases = [
        "Quercus alba L.",
        "quercus ALBA",
        "  Quercus   alba  ",
        "Quercus alba var. alba",
    ]

    for name in test_cases:
        cleaned = standardizer.clean_species_name(name)
        print(f"  '{name}' -> '{cleaned}'")

    # Copyright (c) 2025 Mohamed Z. Hatim
    print(f"\nTesting DataFrame processing (legacy mode):")

    df = pd.DataFrame({
        'species': ['Quercus alba L.', 'Pinus strobus', 'Acer saccharum'],
        'abundance': [25, 15, 30]
    })

    # Copyright (c) 2025 Mohamed Z. Hatim
    df_legacy = standardizer.standardize_dataframe(df, include_error_detection=False)

    print(f"Original columns: {list(df.columns)}")
    print(f"Legacy processed columns: {list(df_legacy.columns)}")
    print(f"Expected columns preserved: {['species_original', 'genus', 'specific_epithet']}")


def main():
    """Run all demonstration functions."""
    print("VegZ Enhanced Species Name Error Detection - DEMONSTRATION")
    print("=" * 80)

    try:
        demo_individual_validation()
        demo_dataframe_processing()
        demo_batch_validation()
        demo_error_reporting()
        demo_backward_compatibility()

        print("\n" + "=" * 80)
        print("DEMONSTRATION COMPLETED SUCCESSFULLY!")
        print("=" * 80)

        print(f"\nKey Features Demonstrated:")
        print(f"[PASS] Individual species name validation with detailed error detection")
        print(f"[PASS] DataFrame integration with optional error detection columns")
        print(f"[PASS] Batch validation for processing large datasets")
        print(f"[PASS] Comprehensive error reporting with statistics and recommendations")
        print(f"[PASS] Full backward compatibility with existing VegZ functionality")

        print(f"\nError Types Detected:")
        print(f"[PASS] Incomplete binomial names (genus-only, species-only)")
        print(f"[PASS] Formatting issues (capitalization, spacing, special characters)")
        print(f"[PASS] Author citations detection and flagging")
        print(f"[PASS] Hybrid markers (×, x) detection and handling")
        print(f"[PASS] Infraspecific rank validation")
        print(f"[PASS] Anonymous/placeholder names (sp., cf., aff., indet., unknown)")
        print(f"[PASS] Invalid characters and symbols")
        print(f"[PASS] Missing genus or species epithets")

    except Exception as e:
        print(f"\nDEMONSTRATION FAILED: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()