"""
OptiPFair: A library for structured pruning of large language models.

This library implements various pruning techniques for transformer-based language models,
with a focus on maintaining model performance while reducing parameter count.
"""

import logging
from typing import Optional, Union, Dict, Any
from transformers import PreTrainedModel

from .pruning.mlp_glu import prune_model_mlp_glu
from .pruning.depth import prune_model_depth, analyze_layer_importance

from .pruning.utils import get_pruning_statistics

__version__ = "0.1.5"

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

def prune_model(
    model: PreTrainedModel,
    pruning_type: str = "MLP_GLU",
    neuron_selection_method: str = "MAW",
    pruning_percentage: Optional[float] = 10,
    expansion_rate: Optional[float] = None,
    show_progress: bool = True,
    return_stats: bool = False,
    # Depth pruning parameters
    num_layers_to_remove: Optional[int] = None,
    layer_indices: Optional[list] = None,
    depth_pruning_percentage: Optional[float] = None,
    layer_selection_method: str = "last",
) -> Union[PreTrainedModel, Dict[str, Any]]:
    """
    Prune a pre-trained language model using the specified pruning method.
    
    Args:
        model: Pre-trained model to prune
        pruning_type: Type of pruning to apply ("MLP_GLU" or "DEPTH")
        neuron_selection_method: Method to calculate neuron importance ("MAW", "VOW", or "PON") - for MLP_GLU only
        pruning_percentage: Percentage of neurons to prune (0-100) - for MLP_GLU only
        expansion_rate: Target expansion rate in percentage (mutually exclusive with pruning_percentage) - for MLP_GLU only
        show_progress: Whether to show progress during pruning
        return_stats: Whether to return pruning statistics along with the model
        num_layers_to_remove: Number of layers to remove - for DEPTH only
        layer_indices: Specific layer indices to remove - for DEPTH only
        depth_pruning_percentage: Percentage of layers to remove - for DEPTH only
        layer_selection_method: Method for selecting layers ("last", "first", "custom") - for DEPTH only
        
    Returns:
        Pruned model or tuple of (pruned_model, statistics) if return_stats is True
    """
    # Keep a copy of the original model parameters for statistics
    original_param_count = None
    if return_stats:
        from copy import deepcopy
        original_model = deepcopy(model)
    
    # Apply the requested pruning method
    if pruning_type == "MLP_GLU":
        pruned_model = prune_model_mlp_glu(
            model=model,
            neuron_selection_method=neuron_selection_method,
            pruning_percentage=pruning_percentage,
            expansion_rate=expansion_rate,
            show_progress=show_progress,
        )
    elif pruning_type == "DEPTH":
        pruned_model = prune_model_depth(
            model=model,
            num_layers_to_remove=num_layers_to_remove,
            layer_indices=layer_indices,
            depth_pruning_percentage=depth_pruning_percentage,
            layer_selection_method=layer_selection_method,
            show_progress=show_progress,
        )
    else:
        supported_types = ["MLP_GLU", "DEPTH"]
        raise ValueError(f"Unsupported pruning type: {pruning_type}. Choose from {supported_types}.")
    
    # Return statistics if requested
    if return_stats:
        stats = get_pruning_statistics(original_model, pruned_model)
        return pruned_model, stats
    
    return pruned_model