#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EPyR Tools - Baseline Correction Package
=======================================

Modern, modular baseline correction for EPR spectroscopy data.

This package provides a comprehensive suite of baseline correction methods
specifically designed for EPR data from epyr.eprload():

Features:
---------
• **Polynomial correction**: For smooth baseline drifts in CW EPR spectra
• **Stretched exponential**: For T2 relaxation and echo decay measurements  
• **Bi-exponential**: For complex decay patterns with multiple components
• **Automatic model selection**: Intelligent model choice using AIC/BIC/R² criteria
• **Interactive region selection**: Manual region specification with matplotlib widgets
• **2D baseline correction**: Surface fitting for 2D EPR datasets

Quick Start:
-----------
```python
import epyr

# Load EPR data
x, y, params, filepath = epyr.eprload("data.dsc")

# Automatic baseline correction (recommended)
corrected, baseline, info = epyr.baseline.baseline_auto_1d(x, y, params)
print(f"Best model: {info['best_model']}")

# Or use specific correction methods:
corrected, baseline = epyr.baseline.baseline_polynomial_1d(x, y, params, order=3)
corrected, baseline = epyr.baseline.baseline_stretched_exponential_1d(x, y, params)
corrected, baseline = epyr.baseline.baseline_bi_exponential_1d(x, y, params)
```

Modules:
--------
• `models`: Mathematical functions for baseline fitting
• `correction`: Core baseline correction algorithms  
• `selection`: Region selection and masking utilities
• `interactive`: Interactive matplotlib widgets for Jupyter
• `auto`: Automatic model selection and comparison
"""

# Import core correction functions
from .correction import (
    baseline_polynomial_1d,
    baseline_polynomial_2d,
    baseline_stretched_exponential_1d,
    baseline_bi_exponential_1d
)

# Import automatic selection
from .auto import (
    baseline_auto_1d,
    compare_models_detailed,
    get_model_recommendations,
    auto_baseline_with_recommendations
)

# Import mathematical models
from .models import (
    stretched_exponential_1d,
    bi_exponential_1d,
    polynomial_1d,
    polynomial_2d,
    exponential_1d,
    get_model_function,
    list_available_models,
    MODEL_INFO
)

# Import region selection utilities
from .selection import (
    create_region_mask_1d,
    create_region_mask_2d,
    get_baseline_regions_1d,
    get_baseline_regions_2d,
    validate_regions_1d,
    validate_regions_2d
)

# Import interactive components
from .interactive import (
    RegionSelector,
    interactive_select_regions_1d,
    interactive_select_regions_2d,
    close_selector_window,
    jupyter_help,
    is_interactive_available,
    setup_interactive_backend
)

# Package metadata
__version__ = "2.0.0"
__author__ = "EPyR Tools Development Team"

# Define comprehensive public API
__all__ = [
    # Core correction functions (most commonly used)
    'baseline_polynomial_1d',
    'baseline_polynomial_2d', 
    'baseline_stretched_exponential_1d',
    'baseline_bi_exponential_1d',
    'baseline_auto_1d',
    
    # Mathematical models
    'stretched_exponential_1d',
    'bi_exponential_1d',
    'polynomial_1d',
    'polynomial_2d',
    'exponential_1d',
    
    # Region selection
    'create_region_mask_1d',
    'create_region_mask_2d',
    'RegionSelector',
    
    # Interactive tools
    'interactive_select_regions_1d',
    'interactive_select_regions_2d',
    'close_selector_window',
    'jupyter_help',
    'is_interactive_available',
    'setup_interactive_backend',
    
    # Advanced features
    'compare_models_detailed',
    'get_model_recommendations',
    'auto_baseline_with_recommendations',
    'get_model_function',
    'list_available_models',
    
    # Utilities
    'get_baseline_regions_1d',
    'get_baseline_regions_2d',
    'validate_regions_1d',
    'validate_regions_2d',
    'MODEL_INFO',
    
    # Backend control
    'setup_inline_backend',
    'setup_widget_backend', 
    'setup_notebook_backend',
    'configure',
    'get_configuration'
]


def get_help():
    """Display comprehensive help for the baseline correction package."""
    help_text = """
    📋 EPyR Baseline Correction Package - Help
    ========================================
    
    🎯 QUICK START - MOST COMMON USAGE:
    
    # Automatic model selection (RECOMMENDED)
    corrected, baseline, info = epyr.baseline.baseline_auto_1d(x, y, params)
    print(f"Best model: {info['best_model']}")
    
    # Manual model selection
    corrected, baseline = epyr.baseline.baseline_polynomial_1d(x, y, params, order=3)
    corrected, baseline = epyr.baseline.baseline_stretched_exponential_1d(x, y, params)
    
    🔧 CORRECTION METHODS:
    
    baseline_polynomial_1d()        - For CW EPR spectra with smooth drifts
    baseline_polynomial_2d()        - For 2D EPR datasets  
    baseline_stretched_exponential_1d()  - For T2 relaxation, echo decay
    baseline_bi_exponential_1d()    - For complex multi-component decay
    baseline_auto_1d()              - Automatic model selection (recommended!)
    
    🖱️  INTERACTIVE SELECTION:
    
    # All correction functions support interactive=True
    corrected, baseline = epyr.baseline.baseline_polynomial_1d(
        x, y, params, interactive=True
    )
    
    # Manual region selection
    from epyr.baseline import RegionSelector
    selector = RegionSelector()
    regions = selector.select_regions_1d(x, y)
    
    📊 DATA TYPE RECOMMENDATIONS:
    
    • CW EPR spectra → baseline_polynomial_1d() 
    • T2 relaxation data → baseline_stretched_exponential_1d()
    • Complex decay → baseline_bi_exponential_1d()
    • Unknown/mixed → baseline_auto_1d()
    
    🆘 JUPYTER NOTEBOOK HELP:
    
    If interactive selection gets stuck:
    from epyr.baseline import close_selector_window
    close_selector_window()
    
    🎨 BACKEND CONTROL:
    
    EPyR baseline now respects your matplotlib backend choice!
    
    # Set inline backend (static plots)
    epyr.baseline.setup_inline_backend()
    # or: %matplotlib inline
    
    # Set interactive backend (zoomable plots)  
    epyr.baseline.setup_widget_backend()
    # or: %matplotlib widget
    
    # Alternative interactive backend
    epyr.baseline.setup_notebook_backend()
    # or: %matplotlib notebook
    
    💡 For more details: help(epyr.baseline.baseline_auto_1d)
    """
    print(help_text)


def demo():
    """Run a demonstration of baseline correction capabilities."""
    print("🎬 EPyR Baseline Correction Demo")
    print("=" * 50)
    
    try:
        import numpy as np
        import matplotlib.pyplot as plt
        
        # Create synthetic test data
        print("📊 Creating synthetic EPR-like data...")
        
        # 1. CW EPR spectrum with polynomial baseline
        x_cw = np.linspace(3300, 3400, 200)
        signal_cw = 50 * np.exp(-((x_cw - 3350) / 10)**2)  # Gaussian signal
        baseline_cw = 0.1 * x_cw**2 - 680 * x_cw + 1150000  # Quadratic drift
        noise_cw = 5 * np.random.normal(size=len(x_cw))
        y_cw = signal_cw + baseline_cw + noise_cw
        
        print("   Testing polynomial correction on synthetic CW EPR...")
        corrected_cw, fitted_baseline = baseline_polynomial_1d(None, y_cw, None, order=2)
        
        # 2. T2 relaxation data with stretched exponential baseline
        x_t2 = np.linspace(0, 2000, 150)
        baseline_t2 = 1000 * np.exp(-((x_t2 / 500)**1.2)) + 50
        noise_t2 = 20 * np.random.normal(size=len(x_t2))
        y_t2 = baseline_t2 + noise_t2
        
        print("   Testing stretched exponential correction on synthetic T2 data...")
        corrected_t2, fitted_t2 = baseline_stretched_exponential_1d(None, y_t2, None)
        
        # 3. Automatic model selection
        print("   Testing automatic model selection...")
        
        test_data = [
            ("CW EPR", None, y_cw),
            ("T2 relaxation", None, y_t2)
        ]
        
        for name, x_data, y_data in test_data:
            try:
                corrected_auto, baseline_auto, info = baseline_auto_1d(
                    x_data, y_data, None, verbose=False
                )
                print(f"   ✅ {name}: Best model = {info['best_model']} (R² = {info['parameters']['r2']:.3f})")
            except Exception as e:
                print(f"   ⚠️  {name}: {e}")
        
        print("\n🎉 Demo completed successfully!")
        print("\n🚀 Available models:", list_available_models())
        print("💡 Run epyr.baseline.get_help() for detailed usage instructions")
        
    except ImportError as e:
        print(f"⚠️  Demo requires numpy and matplotlib: {e}")
    except Exception as e:
        print(f"⚠️  Demo error: {e}")


# Convenience aliases for backward compatibility
# These maintain compatibility with the old baseline_correction.py interface
baseline_auto = baseline_auto_1d
auto_baseline = baseline_auto_1d
polynomial_baseline_1d = baseline_polynomial_1d
polynomial_baseline_2d = baseline_polynomial_2d
stretched_exp_baseline_1d = baseline_stretched_exponential_1d
bi_exp_baseline_1d = baseline_bi_exponential_1d

# Module-level configuration
_DEFAULT_SETTINGS = {
    'polynomial_order': 2,
    'beta_range': (0.01, 5.0),
    'selection_criterion': 'aic',
    'center_fraction': 0.3,
    'interactive_backend': 'manual'  # 'auto', 'widget', 'notebook', 'inline', or 'manual'
}

def configure(**kwargs):
    """
    Configure default settings for baseline correction.
    
    Args:
        polynomial_order: Default polynomial order (default: 2)
        beta_range: Default beta range for stretched exponentials (default: (0.01, 5.0))  
        selection_criterion: Default criterion for automatic selection (default: 'aic')
        center_fraction: Default center exclusion fraction (default: 0.3)
        interactive_backend: Preferred matplotlib backend (default: 'auto')
    """
    for key, value in kwargs.items():
        if key in _DEFAULT_SETTINGS:
            _DEFAULT_SETTINGS[key] = value
        else:
            print(f"⚠️  Unknown configuration option: {key}")
    
    print("✅ Baseline correction settings updated:", _DEFAULT_SETTINGS)

def get_configuration():
    """Get current default settings."""
    return _DEFAULT_SETTINGS.copy()


def setup_inline_backend():
    """Set up inline backend for static plots in Jupyter."""
    try:
        from IPython import get_ipython
        ipython = get_ipython()
        if ipython is not None:
            ipython.magic('matplotlib inline')
            print("✅ Switched to inline backend (static plots)")
        else:
            print("⚠️  Not in Jupyter environment")
    except ImportError:
        print("⚠️  IPython not available")


def setup_widget_backend():
    """Set up widget backend for interactive plots in Jupyter."""
    try:
        from IPython import get_ipython
        ipython = get_ipython()
        if ipython is not None:
            ipython.magic('matplotlib widget')
            print("✅ Switched to widget backend (interactive plots)")
        else:
            print("⚠️  Not in Jupyter environment")
    except ImportError:
        print("⚠️  IPython not available")


def setup_notebook_backend():
    """Set up notebook backend for interactive plots in Jupyter."""
    try:
        from IPython import get_ipython
        ipython = get_ipython()
        if ipython is not None:
            ipython.magic('matplotlib notebook')
            print("✅ Switched to notebook backend (interactive plots)")
        else:
            print("⚠️  Not in Jupyter environment")
    except ImportError:
        print("⚠️  IPython not available")


# Backend setup - only if explicitly requested
# Note: Changed to 'manual' by default to let users choose their preferred backend
try:
    from IPython import get_ipython
    if get_ipython() is not None and _DEFAULT_SETTINGS['interactive_backend'] == 'auto':
        setup_interactive_backend()
except ImportError:
    pass  # Not in Jupyter environment