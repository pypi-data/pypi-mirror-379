API Reference
=============

This section contains the API reference for XRayLabTool's modular architecture.

XRayLabTool is organized into 5 focused sub-packages:

- **calculators**: Core X-ray physics calculations
- **data_handling**: Atomic data caching and batch processing
- **interfaces**: CLI and completion systems
- **validation**: Input validation and error handling
- **io_operations**: File operations and export functionality
- **utils**: Utility functions and constants

.. toctree::
   :maxdepth: 2
   :caption: Core API

   calculators
   data_handling
   interfaces
   validation
   io_operations
   utils
   constants

High-Level Interface
--------------------

The primary entry points for most users:

.. currentmodule:: xraylabtool

Main Calculation Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: calculate_single_material_properties
   :no-index:

.. autofunction:: calculate_xray_properties
   :no-index:


Quick Reference
---------------

**Single Material Calculation:**

.. code-block:: python

   import xraylabtool as xrt

   result = xrt.calculate_single_material_properties(
       formula="Si",
       density=2.33,
       energy=8000
   )

**Batch Calculation:**

.. code-block:: python

   materials = [
       {"formula": "Si", "density": 2.33},
       {"formula": "Al", "density": 2.70}
   ]
   energies = [5000, 8000, 10000]

   results = xrt.calculate_xray_properties(materials, energies)

**Formula Parsing:**

.. code-block:: python

   from xraylabtool.utils import parse_formula

   composition = parse_formula("SiO2")
   # Returns: {"Si": 1, "O": 2}

**Unit Conversions:**

.. code-block:: python

   from xraylabtool.utils import energy_to_wavelength, wavelength_to_energy

   wavelength = energy_to_wavelength(8000)  # eV to Angstrom
   energy = wavelength_to_energy(1.55)      # Angstrom to eV

Exception Hierarchy
-------------------

.. autoclass:: xraylabtool.exceptions.XRayLabToolError
   :members:
   :show-inheritance:
   :no-index:

.. autoclass:: xraylabtool.exceptions.ValidationError
   :members:
   :show-inheritance:
   :no-index:

.. autoclass:: xraylabtool.exceptions.FormulaError
   :members:
   :show-inheritance:
   :no-index:

.. autoclass:: xraylabtool.exceptions.EnergyError
   :members:
   :show-inheritance:
   :no-index:

.. autoclass:: xraylabtool.exceptions.CalculationError
   :members:
   :show-inheritance:
   :no-index:
