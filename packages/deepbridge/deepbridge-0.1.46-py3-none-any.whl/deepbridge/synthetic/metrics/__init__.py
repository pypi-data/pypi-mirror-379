"""
Metrics for evaluating synthetic data quality.

This module provides various metrics and functions for evaluating
the quality of synthetic data compared to the original real data.

Key components:
- Statistical: Statistical comparison metrics
- Similarity: Analysis of record-level similarity 
- Privacy: Privacy risk assessment
- Utility: Utility preservation evaluation
- SyntheticMetrics: Comprehensive evaluation toolkit

Usage:
    from synthetic.metrics import SyntheticMetrics
    
    # Create metrics evaluator
    metrics = SyntheticMetrics(
        real_data=original_df,
        synthetic_data=synthetic_df
    )
    
    # Get overall quality score
    quality_score = metrics.overall_quality()
    
    # Print summary
    metrics.print_summary()
    
    # Access individual metric functions
    from synthetic.metrics import evaluate_synthetic_quality, calculate_similarity
    
    # Evaluate just statistical metrics
    stat_metrics = evaluate_synthetic_quality(real_data, synthetic_data)
    
    # Calculate similarity scores
    similarity_scores = calculate_similarity(real_data, synthetic_data)
"""

# Statistical metrics
from .statistical import evaluate_synthetic_quality, evaluate_numerical_column, evaluate_categorical_column, print_quality_metrics

# Similarity metrics
from .similarity import calculate_similarity, filter_by_similarity, detect_duplicates, calculate_diversity

# Privacy metrics
from .privacy import assess_k_anonymity, assess_l_diversity, assess_membership_disclosure

# Utility metrics
from .utility import evaluate_machine_learning_utility, evaluate_statistical_fidelity, evaluate_query_errors

# Comprehensive metrics class
from .synthetic_metrics import SyntheticMetrics