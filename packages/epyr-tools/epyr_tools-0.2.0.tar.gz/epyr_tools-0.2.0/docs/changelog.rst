Changelog
=========

All notable changes to EPyR Tools are documented here.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[0.1.6] - 2025-09-12
---------------------

Added
~~~~~
- **NEW:** Comprehensive testing protocol with 4 levels (SMOKE, STANDARD, DEEP, SCIENTIFIC)
- **NEW:** Deep testing infrastructure with automated test runners
- **NEW:** Complete lineshape analysis system with mathematical validation
- **NEW:** Performance benchmarking for all core functions
- **NEW:** Scientific accuracy validation against NIST standards

Changed
~~~~~~~
- **BREAKING:** Removed all numbered notebooks from examples/ for cleaner project structure
- **IMPROVEMENT:** Removed all emojis from documentation for professional appearance
- **UPDATE:** Version updated to 0.1.6 across all configuration files
- **ENHANCEMENT:** Updated documentation with comprehensive testing information
- **FIX:** Fixed pseudo_voigt parameter handling in lineshape_class

Removed
~~~~~~~
- Removed numbered example notebooks (01_, 04_, 05_, 06_, 07_, 08_, 09_, 10_)
- Cleaned emojis from all markdown documentation files

Fixed
~~~~~
- Fixed voigtian function calls with proper parameter structure
- Corrected lineshape function parameter handling
- Updated all version references to 0.1.6

[0.1.2] - 2025-09-05
---------------------

Removed
~~~~~~~
- **BREAKING:** Removed ``epyr.sub.baseline2.py`` - deprecated duplicate baseline functions
- **BREAKING:** Removed ``epyr.sub.processing2.py`` - deprecated duplicate processing functions
- Cleaned up duplicate code and imports

Changed
~~~~~~~
- Updated package imports to remove references to deleted modules
- All baseline correction functions now available through ``epyr.baseline`` module
- Streamlined package structure for better maintainability

Fixed
~~~~~
- Fixed import issues in Getting Started notebook
- Consolidated all data files into single ``examples/data/`` directory
- Fixed complex data handling in notebooks
- Updated path detection for cross-platform compatibility

Documentation
~~~~~~~~~~~~~
- Updated README with version badge
- Created comprehensive Getting Started notebook with real data examples
- Added proper error handling and troubleshooting in notebook
- Updated all version references

Migration Guide
~~~~~~~~~~~~~~~
If you were using the removed modules:

.. code-block:: python

   # OLD (no longer works)
   from epyr.sub.baseline2 import baseline_polynomial
   from epyr.sub.processing2 import baseline_polynomial

   # NEW (use instead)
   from epyr.baseline import baseline_polynomial

[0.1.1] - 2025-09-04
---------------------

Added
~~~~~
- Comprehensive README with professional documentation
- Setup.py for pip package installation
- Example notebooks and tutorials
- FAIR data conversion capabilities
- Advanced plotting functionality

Fixed
~~~~~
- Various import and compatibility issues
- Documentation generation
- Test coverage improvements

[0.1.0] - 2025-09-01
---------------------

Added
~~~~~
- Initial release
- EPR data loading (BES3T and ESP formats)
- Basic baseline correction
- Constants and physical parameters
- Isotope GUI application
- Basic plotting capabilities

Features by Version
-------------------

Core Data Loading
~~~~~~~~~~~~~~~~~

**Version 0.1.0+**

- Load BES3T (.dsc/.dta) files from modern Bruker spectrometers
- Load ESP (.par/.spc) files from legacy Bruker systems
- Automatic format detection and parameter extraction
- Support for both 1D spectra and 2D datasets
- Complex data handling for pulsed EPR experiments

**Version 0.1.1+**

- Enhanced error handling and validation
- Cross-platform file path compatibility
- Improved parameter parsing and units

**Version 0.1.2+**

- Consolidated data directory structure
- Enhanced 2D data support in examples
- Better complex data visualization

FAIR Data Conversion
~~~~~~~~~~~~~~~~~~~~

**Version 0.1.1+**

- Convert to CSV format with metadata headers
- Export to JSON with complete parameter documentation
- Save as HDF5 for efficient large dataset storage
- Preserve all experimental metadata
- Cross-platform compatibility

Advanced Baseline Correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Version 0.1.0+**

- Polynomial baseline correction (orders 0-5)
- Signal region exclusion from baseline fitting
- 1D spectrum processing with validation

**Version 0.1.1+**

- Exponential decay models (single and stretched)
- Improved parameter estimation algorithms
- Better error handling for edge cases

**Version 0.1.2+**

- Streamlined API through unified ``epyr.baseline`` module
- Removed duplicate and deprecated functions
- Enhanced documentation and examples

Visualization Tools
~~~~~~~~~~~~~~~~~~~

**Version 0.1.0+**

- Basic EPR spectrum plotting
- Parameter display and annotation
- Export to common image formats

**Version 0.1.1+**

- 2D spectral maps with customizable color schemes
- Interactive plotting capabilities
- Publication-quality output options

**Version 0.1.2+**

- Enhanced 2D data visualization in examples
- Complex data magnitude plotting
- Improved axis labeling and units

Documentation and Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Version 0.1.0+**

- Basic API documentation with Sphinx
- Simple usage examples
- Core function docstrings

**Version 0.1.1+**

- Comprehensive README with installation guide
- Professional Sphinx documentation theme
- Tutorial notebooks for interactive learning

**Version 0.1.2+**

- Complete ReadTheDocs.io integration
- Detailed installation and contribution guides
- Enhanced example scripts and notebooks
- Cross-referenced API documentation

Development Infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Version 0.1.0+**

- Basic package structure
- Essential dependencies (NumPy, Matplotlib, SciPy)
- Git version control

**Version 0.1.1+**

- Standard setup.py for pip installation
- Development dependencies and tools
- Code quality checks (Black, isort, flake8)

**Version 0.1.2+**

- Pre-commit hooks for automated code quality
- Comprehensive test suite (44 tests)
- Modern packaging with pyproject.toml
- ReadTheDocs configuration for automatic documentation builds

Deprecation Notices
-------------------

Version 0.1.2
~~~~~~~~~~~~~~

The following modules were removed as they contained duplicate functionality:

- ``epyr.sub.baseline2`` - Use ``epyr.baseline`` instead
- ``epyr.sub.processing2`` - Functionality merged into main modules

These modules were deprecated since version 0.1.1 and have been removed to streamline the package structure.

Future versions will maintain backward compatibility for the public API in ``epyr.baseline``, ``epyr.eprload``, and ``epyr.fair`` modules.

Upgrade Path
------------

From 0.1.1 to 0.1.2
~~~~~~~~~~~~~~~~~~~~

1. **Update imports:**

   .. code-block:: python

      # Change this:
      from epyr.sub.baseline2 import baseline_polynomial

      # To this:
      from epyr.baseline import baseline_polynomial

2. **Update data paths:** If you were using separate ``BES3T/`` and ``ESP/`` directories, consolidate data files into a single directory.

3. **Check examples:** Updated example scripts now handle both 1D and 2D data automatically.

From 0.1.0 to 0.1.1
~~~~~~~~~~~~~~~~~~~~

No breaking changes - all existing code should continue to work.

New features can be adopted incrementally:

- Use ``epyr.fair`` module for data conversion
- Try new example notebooks in ``examples/notebooks/``
- Install with ``pip install -e .`` for easier development

Breaking Changes by Version
---------------------------

Version 0.1.2
~~~~~~~~~~~~~~

- Removed ``epyr.sub.baseline2`` module
- Removed ``epyr.sub.processing2`` module
- Changed example data directory structure

Version 0.1.1
~~~~~~~~~~~~~~

No breaking changes from 0.1.0.

Version 0.1.0
~~~~~~~~~~~~~~

Initial release - no previous versions to break compatibility with.
