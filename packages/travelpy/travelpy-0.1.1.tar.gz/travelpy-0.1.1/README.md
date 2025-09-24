# travelpy

Python wrapper for TRAVEL particle tracking simulations.

## Overview

travelpy provides a modern Python interface to the TRAVEL particle tracking code, making it easier to:

- Run TRAVEL simulations from Python scripts or Jupyter notebooks
- Analyze beam and beamline files programmatically
- Process simulation outputs and visualize results
- Automate parameter sweeps and optimization studies

## Quick Start

```python
import travelpy as tp

# Configure TRAVEL path (one-time setup, if needed)
tp.set_travel_directory("C:/Program Files (x86)/Path Manager/Travel")

# Run a simulation
result = tp.run_travel("beam.dat", "beamline.in")

# Display output files
result.display_output_files()

# Access simulation data with simple properties
avgout = result.avgout
rmsout = result.rmsout

# Analyze key results
print(f"Final transmission: {avgout.transmission.iloc[-1]:.1f}%")
print(f"Final beam energy: {avgout.ekin_avg.iloc[-1]*1000:.1f} MeV")
print(f"Horizontal emittance: {rmsout.emitt_norm_rms_x_xp.iloc[-1]*1e6:.2f} mm·mrad")

# Clean up output files when done
result.clean_outputs()
```

## Installation

```bash
pip install travelpy
```

## Requirements

- Python 3.10+
- TRAVEL simulation code (Windows only)
- NumPy, matplotlib

## Examples and Tutorials

The `examples/` folder contains comprehensive tutorials designed for newcomers to travelpy. These hands-on examples cover everything from basic simulation workflows to advanced features like parameter sweeps and parallel processing. Each example is self-contained with sample data and step-by-step explanations to help you get started quickly.

## Documentation

Full documentation with examples and API reference coming soon.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## License

MIT License - see [LICENSE](LICENSE) file for details.
