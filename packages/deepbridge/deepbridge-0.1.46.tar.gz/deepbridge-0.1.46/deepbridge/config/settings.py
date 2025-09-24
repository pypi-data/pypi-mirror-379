from typing import List, Optional
import logging
import os
from deepbridge.utils.model_registry import ModelType

class DistillationConfig:
    """
    Configuration manager for knowledge distillation parameters.

    Manages model types, temperatures, alphas, and general configuration
    for automated distillation experiments.
    """

    def __init__(
        self,
        output_dir: str = "distillation_results",
        test_size: float = 0.2,
        random_state: int = 42,
        n_trials: int = 10,
        validation_split: float = 0.2,
        verbose: bool = True,
        distillation_method: str = "surrogate",
        # HPM-specific parameters
        use_hpm: bool = False,
        max_configs: int = 16,
        parallel_workers: Optional[int] = None,
        use_cache: bool = True,
        use_progressive: bool = True,
        use_multi_teacher: bool = True,
        use_adaptive_temperature: bool = True,
        cache_memory_gb: float = 2.0
    ):
        """
        Initialize distillation configuration.

        Args:
            output_dir: Directory to save results and visualizations
            test_size: Fraction of data to use for testing
            random_state: Random seed for reproducibility
            n_trials: Number of Optuna trials for hyperparameter optimization
            validation_split: Fraction of data to use for validation during optimization
            verbose: Whether to show progress messages
            distillation_method: Method to use for distillation ('surrogate', 'knowledge_distillation', 'hpm')
            use_hpm: Whether to use HPM-KD optimizations
            max_configs: Maximum number of configurations for HPM
            parallel_workers: Number of parallel workers (None for auto)
            use_cache: Enable intelligent caching
            use_progressive: Enable progressive distillation chain
            use_multi_teacher: Enable multi-teacher ensemble
            use_adaptive_temperature: Enable adaptive temperature scheduling
            cache_memory_gb: Maximum memory for cache in GB
        """
        self.output_dir = output_dir
        self.test_size = test_size
        self.random_state = random_state
        self.n_trials = n_trials
        self.validation_split = validation_split
        self.verbose = verbose
        self.distillation_method = distillation_method

        # HPM-specific parameters
        self.use_hpm = use_hpm
        self.max_configs = max_configs
        self.parallel_workers = parallel_workers
        self.use_cache = use_cache
        self.use_progressive = use_progressive
        self.use_multi_teacher = use_multi_teacher
        self.use_adaptive_temperature = use_adaptive_temperature
        self.cache_memory_gb = cache_memory_gb

        # Set default configuration
        self._set_default_config()

        # Configure logging
        self._configure_logging()

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
    
    def _set_default_config(self):
        """Set default configuration for model types, temperatures, and alphas."""
        self.model_types = [
            ModelType.LOGISTIC_REGRESSION,
            ModelType.DECISION_TREE,
            ModelType.GBM,
            ModelType.XGB
        ]
        
        self.temperatures = [0.5, 1.0, 2.0, 3.0]
        self.alphas = [0.3, 0.5, 0.7, 0.9]
    
    def _configure_logging(self):
        """Configure logging based on verbosity setting."""
        if not self.verbose:
            optuna_logger = logging.getLogger("optuna")
            optuna_logger.setLevel(logging.ERROR)
    
    def customize(
        self,
        model_types: Optional[List[ModelType]] = None,
        temperatures: Optional[List[float]] = None,
        alphas: Optional[List[float]] = None,
        distillation_method: Optional[str] = None
    ):
        """
        Customize the configuration for distillation experiments.
        
        Args:
            model_types: List of ModelType to test (defaults to standard list if None)
            temperatures: List of temperature values to test (defaults to [0.5, 1.0, 2.0] if None)
            alphas: List of alpha values to test (defaults to [0.3, 0.5, 0.7] if None)
            distillation_method: Method to use for distillation ('surrogate' or 'knowledge_distillation')
        """
        if model_types is not None:
            self.model_types = model_types
        if temperatures is not None:
            self.temperatures = temperatures
        if alphas is not None:
            self.alphas = alphas
        if distillation_method is not None:
            self.distillation_method = distillation_method
    
    def get_total_configurations(self) -> int:
        """
        Calculate total number of configurations to test.
        
        Returns:
            Total number of configurations
        """
        return len(self.model_types) * len(self.temperatures) * len(self.alphas)
    
    def log_info(self, message: str):
        """
        Log information if verbose mode is enabled.
        
        Args:
            message: Message to log
        """
        if self.verbose:
            print(message)