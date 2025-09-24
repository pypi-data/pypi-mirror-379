#!/usr/bin/env python3
"""
Convert VegZ Testing Suite to Jupyter Notebook
"""

import json

def create_jupyter_notebook():
    """Create a Jupyter notebook from the testing functions"""

    # Copyright (c) 2025 Mohamed Z. Hatim
    notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

    # Copyright (c) 2025 Mohamed Z. Hatim
    cells_content = [
        {
            "title": "Cell 1: Package Import and Setup",
            "code": '''# Copyright (c) 2025 Mohamed Z. Hatim
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Copyright (c) 2025 Mohamed Z. Hatim
import VegZ as VegZ_module

# Copyright (c) 2025 Mohamed Z. Hatim
from VegZ import VegZ as VegZClass, quick_diversity_analysis, quick_ordination, quick_clustering, quick_elbow_analysis
from VegZ.diversity import DiversityAnalyzer
from VegZ.multivariate import MultivariateAnalyzer
from VegZ.clustering import VegetationClustering
from VegZ.statistics import EcologicalStatistics
from VegZ.temporal import TemporalAnalyzer
from VegZ.spatial import SpatialAnalyzer
from VegZ.environmental import EnvironmentalModeler
from VegZ.machine_learning import MachineLearningAnalyzer, PredictiveModeling
from VegZ.functional_traits import FunctionalTraitAnalyzer, TraitSyndromes
from VegZ.nestedness import NestednessAnalyzer, NullModels
from VegZ.specialized_methods import PhylogeneticDiversityAnalyzer, MetacommunityAnalyzer, NetworkAnalyzer
from VegZ.interactive_viz import InteractiveVisualizer, ReportGenerator
from VegZ import data_management, data_quality

# Copyright (c) 2025 Mohamed Z. Hatim
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Copyright (c) 2025 Mohamed Z. Hatim
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("✓ VegZ successfully imported!")
print(f"✓ VegZ version: {VegZ_module.__version__}")

# Copyright (c) 2025 Mohamed Z. Hatim
print("\\nAvailable VegZ modules:")
print("- Core functionality: VegZ main class")
print("- Diversity analysis: DiversityAnalyzer")
print("- Multivariate analysis: MultivariateAnalyzer")
print("- Clustering: VegetationClustering")
print("- Statistics: EcologicalStatistics")
print("- Specialized methods: Multiple specialized analyzers")

# Copyright (c) 2025 Mohamed Z. Hatim
VegZ = VegZClass'''
        },

        {
            "title": "Cell 2: Data Loading and Inspection",
            "code": '''# Copyright (c) 2025 Mohamed Z. Hatim
print("Loading test datasets...\\n")

# Copyright (c) 2025 Mohamed Z. Hatim
vegetation_data = pd.read_csv('test_data/vegetation_survey_data.csv')
print(f"✓ Vegetation survey data: {vegetation_data.shape}")

# Copyright (c) 2025 Mohamed Z. Hatim
species_abundance = pd.read_csv('test_data/species_abundance.csv', index_col=0)
print(f"✓ Species abundance matrix: {species_abundance.shape}")

# Copyright (c) 2025 Mohamed Z. Hatim
environmental_data = pd.read_csv('test_data/environmental_variables.csv', index_col=0)
print(f"✓ Environmental variables: {environmental_data.shape}")

# Copyright (c) 2025 Mohamed Z. Hatim
species_traits = pd.read_csv('test_data/species_traits.csv', index_col=0)
print(f"✓ Species traits: {species_traits.shape}")

# Copyright (c) 2025 Mohamed Z. Hatim
phylo_distances = pd.read_csv('test_data/phylogenetic_distances.csv', index_col=0)
print(f"✓ Phylogenetic distances: {phylo_distances.shape}")

# Copyright (c) 2025 Mohamed Z. Hatim
print("\\n" + "="*50)
print("DATA STRUCTURE OVERVIEW")
print("="*50)

print("\\n1. Vegetation Survey Data (first 5 rows):")
print(vegetation_data.head())

print("\\n2. Species Abundance Matrix (first 5 rows, 10 columns):")
print(species_abundance.iloc[:5, :10])

print("\\n3. Environmental Variables:")
print(environmental_data.head())

print("\\n4. Species Traits (first 5 species):")
print(species_traits.head())

print("\\n5. Data Summary Statistics:")
print(f"- Number of sites: {len(species_abundance)}")
print(f"- Number of species: {len(species_abundance.columns)}")
print(f"- Number of environmental variables: {len(environmental_data.columns)}")
print(f"- Total abundance across all sites: {species_abundance.sum().sum()}")
print(f"- Mean species richness per site: {(species_abundance > 0).sum(axis=1).mean():.1f}")'''
        },

        {
            "title": "Cell 3: Initialize VegZ and Basic Setup",
            "code": '''# Copyright (c) 2025 Mohamed Z. Hatim
veg = VegZ()
veg.data = species_abundance
veg.species_matrix = species_abundance
veg.environmental_data = environmental_data

print("✓ VegZ initialized with test data")
print(f"✓ Species matrix shape: {veg.species_matrix.shape}")
print(f"✓ Environmental data shape: {veg.environmental_data.shape}")

# Copyright (c) 2025 Mohamed Z. Hatim
summary_stats = veg.summary_statistics()
print("\\n" + "="*50)
print("DATASET SUMMARY STATISTICS")
print("="*50)
for key, value in summary_stats.items():
    if isinstance(value, (int, float)):
        print(f"{key}: {value}")
    elif hasattr(value, 'describe'):
        print(f"\\n{key}:")
        print(value)'''
        },

        {
            "title": "Cell 4: Comprehensive Diversity Analysis",
            "code": '''# Copyright (c) 2025 Mohamed Z. Hatim
print("="*60)
print("COMPREHENSIVE DIVERSITY ANALYSIS")
print("="*60)

# Copyright (c) 2025 Mohamed Z. Hatim
diversity_indices = veg.calculate_diversity([
    'shannon', 'simpson', 'richness', 'evenness'
])

print("1. Basic Diversity Indices (VegZ Core):")
print(diversity_indices.head())
print(f"\\nDiversity indices shape: {diversity_indices.shape}")

# Copyright (c) 2025 Mohamed Z. Hatim
diversity_analyzer = DiversityAnalyzer()

# Copyright (c) 2025 Mohamed Z. Hatim
try:
    all_diversity = diversity_analyzer.calculate_all_indices(species_abundance)
    print(f"\\n2. All Available Diversity Indices ({len(all_diversity.columns)} indices):")
    print(all_diversity.head())
    print(f"Available diversity indices: {diversity_analyzer.available_indices}")
except Exception as e:
    print(f"⚠ All diversity indices calculation: {e}")

# Copyright (c) 2025 Mohamed Z. Hatim
try:
    print("\\n5. Rarefaction Analysis:")
    rarefaction_data = veg.rarefaction_curve()
    print(f"Rarefaction data shape: {rarefaction_data.shape}")
    print("Sample of rarefaction data:")
    print(rarefaction_data.head(10))
except Exception as e:
    print(f"⚠ Rarefaction analysis: {e}")'''
        },

        {
            "title": "Cell 5: Quick Functions Testing",
            "code": '''# Copyright (c) 2025 Mohamed Z. Hatim
print("="*60)
print("QUICK ANALYSIS FUNCTIONS TESTING")
print("="*60)

# Copyright (c) 2025 Mohamed Z. Hatim
print("1. Quick Diversity Analysis")
try:
    quick_div = quick_diversity_analysis(species_abundance)
    print("✓ Quick diversity analysis completed")
    print(f"Shape: {quick_div.shape}")
    print("First 5 rows:")
    print(quick_div.head())
except Exception as e:
    print(f"⚠ Quick diversity analysis: {e}")

# Copyright (c) 2025 Mohamed Z. Hatim
print("\\n2. Quick Ordination Analysis")
try:
    quick_pca = quick_ordination(species_abundance, method='pca')
    print("✓ Quick PCA completed")
    print(f"Explained variance ratio: {quick_pca['explained_variance_ratio'][:3]}")
    print(f"PCA scores shape: {quick_pca['scores'].shape}")
except Exception as e:
    print(f"⚠ Quick PCA: {e}")

# Copyright (c) 2025 Mohamed Z. Hatim
print("\\n3. Quick Clustering Analysis")
try:
    quick_kmeans = quick_clustering(species_abundance, n_clusters=4, method='kmeans')
    print("✓ Quick K-means completed")
    print(f"Inertia: {quick_kmeans['inertia']:.2f}")
    print("Cluster distribution:")
    print(quick_kmeans['cluster_labels'].value_counts().sort_index())
except Exception as e:
    print(f"⚠ Quick K-means: {e}")

# Copyright (c) 2025 Mohamed Z. Hatim
print("\\n4. Quick Elbow Analysis")
try:
    quick_elbow = quick_elbow_analysis(species_abundance, max_k=8, plot_results=True)
    print("✓ Quick elbow analysis completed")
    if 'recommendations' in quick_elbow:
        consensus_k = quick_elbow['recommendations']['consensus']
        print(f"Recommended optimal k: {consensus_k}")
except Exception as e:
    print(f"⚠ Quick elbow analysis: {e}")'''
        },

        {
            "title": "Cell 6: Visualization Testing",
            "code": '''# Copyright (c) 2025 Mohamed Z. Hatim
print("="*60)
print("COMPREHENSIVE VISUALIZATION TESTING")
print("="*60)

# Copyright (c) 2025 Mohamed Z. Hatim
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

# Copyright (c) 2025 Mohamed Z. Hatim
print("1. Diversity Visualizations")

# Copyright (c) 2025 Mohamed Z. Hatim
try:
    fig1 = veg.plot_diversity(diversity_indices, 'shannon')
    plt.title('Shannon Diversity Distribution')
    plt.tight_layout()
    plt.show()

    fig2 = veg.plot_diversity(diversity_indices, 'richness')
    plt.title('Species Richness Distribution')
    plt.tight_layout()
    plt.show()

    print("✓ Diversity distribution plots created")
except Exception as e:
    print(f"⚠ Diversity plots: {e}")

# Copyright (c) 2025 Mohamed Z. Hatim
try:
    # Copyright (c) 2025 Mohamed Z. Hatim
    env_vars = ['elevation', 'soil_ph', 'temperature', 'precipitation']
    available_env_vars = [var for var in env_vars if var in environmental_data.columns]

    if len(available_env_vars) >= 2:
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        for i, env_var in enumerate(available_env_vars[:2]):
            axes[i].scatter(environmental_data[env_var], diversity_indices['shannon'], alpha=0.7, s=50)
            axes[i].set_xlabel(env_var.replace('_', ' ').title())
            axes[i].set_ylabel('Shannon Diversity')
            axes[i].set_title(f'Diversity vs {env_var.replace("_", " ").title()}')
            axes[i].grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()
        print("✓ Environmental relationship plots created")

except Exception as e:
    print(f"⚠ Environmental relationship plots: {e}")

print("\\n✓ All visualization testing completed")'''
        }
    ]

    # Copyright (c) 2025 Mohamed Z. Hatim
    for i, cell_content in enumerate(cells_content):
        cell = {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                f"# {cell_content['title']}\\n\\n" + cell_content['code']
            ]
        }
        notebook["cells"].append(cell)

    # Copyright (c) 2025 Mohamed Z. Hatim
    intro_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# VegZ Complete Testing Suite\\n",
            "\\n",
            "This notebook provides comprehensive testing of all VegZ functionalities using test data.\\n",
            "\\n",
            "## Features Tested:\\n",
            "- Package imports and setup\\n",
            "- Data loading and inspection\\n",
            "- VegZ initialization\\n",
            "- Diversity analysis (15+ indices)\\n",
            "- Quick analysis functions\\n",
            "- Comprehensive visualizations\\n",
            "\\n",
            "## Requirements:\\n",
            "- VegZ package installed (`pip install VegZ`)\\n",
            "- Test data files in `test_data/` directory\\n",
            "- Python 3.8+ with required dependencies\\n",
            "\\n",
            "---\\n"
        ]
    }

    # Copyright (c) 2025 Mohamed Z. Hatim
    notebook["cells"].insert(0, intro_cell)

    # Copyright (c) 2025 Mohamed Z. Hatim
    with open('VegZ_Testing_Suite.ipynb', 'w') as f:
        json.dump(notebook, f, indent=2)

    print("SUCCESS: Jupyter notebook created: VegZ_Testing_Suite.ipynb")
    print("You can now open it with: jupyter notebook VegZ_Testing_Suite.ipynb")

if __name__ == "__main__":
    create_jupyter_notebook()