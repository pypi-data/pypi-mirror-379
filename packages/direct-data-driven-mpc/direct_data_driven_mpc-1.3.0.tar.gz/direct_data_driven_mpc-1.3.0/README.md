# Direct Data-Driven Model Predictive Control (MPC)

<div align="center">

[![PyPi](https://img.shields.io/pypi/v/direct-data-driven-mpc)](https://pypi.org/project/direct-data-driven-mpc)
[![CI Workflow status](https://github.com/pavelacamposp/direct-data-driven-mpc/actions/workflows/ci_workflow.yml/badge.svg)](https://github.com/pavelacamposp/direct-data-driven-mpc/actions/workflows/ci_workflow.yml)
[![Docs status](https://img.shields.io/github/actions/workflow/status/pavelacamposp/direct-data-driven-mpc/docs.yml?label=docs&color=brightgreen)](https://github.com/pavelacamposp/direct-data-driven-mpc/actions/workflows/docs.yml)
[![codecov](https://codecov.io/gh/pavelacamposp/direct-data-driven-mpc/graph/badge.svg)](https://codecov.io/gh/pavelacamposp/direct-data-driven-mpc)
[![Ruff](https://img.shields.io/badge/Lint%20%26%20Format-Ruff-blue?logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.12-blue)](https://docs.python.org/3.10)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/license/MIT)

</div>

<table>
  <tr>
    <th width="50%">Robust Data-Driven MPC</th>
    <th width="50%">Nonlinear Data-Driven MPC</th>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/pavelacamposp/direct-data-driven-mpc/main/docs/resources/robust_dd_mpc_anim.gif" alt="Robust Data-Driven MPC Animation"></td>
    <td><img src="https://raw.githubusercontent.com/pavelacamposp/direct-data-driven-mpc/main/docs/resources/nonlinear_dd_mpc_anim.gif" alt="Nonlinear Data-Driven MPC Animation"></td>
  </tr>
  <tr>
    <td>Robust controller applied to an LTI system.</td>
    <td>Nonlinear controller applied to a nonlinear system.</td>
  </tr>
</table>

This repository provides a Python implementation of Direct Data-Driven Model Predictive Control (MPC) controllers for Linear Time-Invariant (LTI) and nonlinear systems using CVXPY. It includes **robust** and **nonlinear** controllers implemented based on the Data-Driven MPC schemes presented in the papers ["Data-Driven Model Predictive Control With Stability and Robustness Guarantees"](https://ieeexplore.ieee.org/document/9109670) and ["Linear Tracking MPC for Nonlinear Systems—Part II: The Data-Driven Case"](https://ieeexplore.ieee.org/document/9756053) by J. Berberich et al.

A **direct data-driven controller** maps measured input-output data from an unknown system *directly* onto the controller without requiring an explicit system identification step. This approach is particularly useful in applications where the system dynamics are too complex to be modeled accurately or where traditional system identification methods are impractical or difficult to apply.

📖 View the full project documentation on our **[documentation page](https://pavelacamposp.github.io/direct-data-driven-mpc)**.

---
***Disclaimer:** This is an independent project based on the referenced papers and does not contain the official implementations from the authors.*

---


## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Paper Reproduction](#paper-reproduction)
- [Code Structure](#code-structure)
  - [Direct Data-Driven MPC Controller](#direct-data-driven-mpc-controller)
  - [Model Simulation](#model-simulation)
  - [Controller Creation](#controller-creation)
  - [Data-Driven Controller Simulation](#data-driven-controller-simulation)
  - [Visualization (Static and Animated Plots)](#visualization-static-and-animated-plots)
  - [Examples](#examples)
  - [Configuration Files](#configuration-files)
- [License](#license)
- [Citation](#citation)

## Requirements
This package requires the following:
- **Python** (>=3.10, <3.13). Python 3.13 is not fully supported, as some dependencies have not been compiled for this version yet. We recommend using Python 3.10 to 3.12.
- **FFmpeg:** Required for saving animations (e.g., GIF or MP4).
    - **On Windows:** You can download FFmpeg from [the official FFmpeg website](https://ffmpeg.org/download.html). Ensure it's correctly added to your system's `PATH`.
    - **On Unix:** You can install it using your package manager. For Debian/Ubuntu:
        ```bash
        sudo apt install ffmpeg
        ```
    Verify the installation by running this command:
    ```bash
    ffmpeg -version
    ```

## Installation
Install `direct-data-driven-mpc` via PyPI:
```bash
pip install direct-data-driven-mpc
```
**Note:** We recommend using a virtual environment to install this package, although it is not required.

### For Contributors:
If you plan to contribute to or develop the project, follow these steps to set up a local development environment:
1. Clone the repository and navigate to the project directory:
    ```bash
    git clone https://github.com/pavelacamposp/direct-data-driven-mpc.git && cd direct-data-driven-mpc
    ```
2. Create and activate a virtual environment:
    - Unix/macOS:
      ```bash
      python3 -m venv .venv && source .venv/bin/activate
      ```
    - Windows:
      ```cmd
      python -m venv venv && venv\Scripts\activate
      ```
3. Install the package with development dependencies:
    ```bash
    pip install -e ".[dev]"
    ```

This will install tools like `pre-commit` and `mypy`. To enable automatic checks before each commit using `pre-commit` hooks, run:
```bash
pre-commit install
```

## Usage
The example scripts [`lti_dd_mpc_example.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/lti_control/lti_dd_mpc_example.py) and [`nonlinear_dd_mpc_example.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/nonlinear_control/nonlinear_dd_mpc_example.py) demonstrate the setup, simulation, and data visualization of the Data-Driven MPC controllers applied to LTI and nonlinear systems, respectively.

To run the example scripts, use the following commands:

- **Data-Driven MPC for LTI systems:**

    Run the example script with a seed of `18`, a simulation length of `400` steps, a verbosity level of `1`, and save the generated animation to a file:

    ```bash
    python examples/lti_control/lti_dd_mpc_example.py --seed 18 --t_sim 400 --verbose 1 --save_anim
    ```

- **Data-Driven MPC for Nonlinear systems:**

    Run the example script with a seed of `0`, a simulation length of `3000` steps, a verbosity level of `1`, and save the generated animation to a file:

    ```bash
    python examples/nonlinear_control/nonlinear_dd_mpc_example.py --seed 0 --t_sim 3000 --verbose 1 --save_anim
    ```

> [!NOTE]
> The `--save_anim` flag requires FFmpeg to be installed. See the [Requirements](#requirements) section for more details.

### Customizing Controller Parameters
To use different controller parameters, modify the configuration files in [`examples/config/controllers/`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/config/controllers/) for each controller, or specify a custom configuration file using the `--controller_config_path` argument.

### Customizing System Models
Example system parameters are defined in [`examples/config/models/`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/config/models/).

- **LTI system:** Parameters can be modified directly in [`four_tank_system_params.yaml`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/config/models/four_tank_system_params.yaml).
- **Nonlinear system:** The system dynamics are defined in [`nonlinear_cstr_model.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/nonlinear_control/utilities/nonlinear_cstr_model.py) and its parameters in [`nonlinear_cstr_system_params.yaml`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/config/models/nonlinear_cstr_system_params.yaml).

### Customizing Plots
Matplotlib properties for input-output plots can be customized by modifying [plot_params.yaml](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/config/plots/plot_params.yaml).

### Additional Information
Some key arguments used in the scripts are listed below:
Argument | Type | Description
--- | --- | ---
`--controller_config_path` | `str` | Path to the YAML file containing Data-Driven MPC controller parameters.
`--t_sim` | `int` | Simulation length in time steps.
`--save_anim` | `flag` | If passed, saves the generated animation to a file using FFmpeg.
`--anim_path` | `str` | Path where the generated animation file will be saved. Includes the file name and its extension (e.g., `data-driven_mpc_sim.gif`).
`--verbose` | `int` | Verbosity level: `0` = no output, `1` = minimal output, `2` = detailed output.

To get the full list of arguments, run each script with the `--help` flag.

---
For a deeper understanding of the project and how the controllers operate, we recommend reading through the scripts and the docstrings of the implemented utility functions and classes. The documentation includes detailed descriptions of how the implementations follow the Data-Driven MPC controller schemes and algorithms described in the referenced papers.

## Paper Reproduction
Reproduction scripts are provided to validate our implementations by comparing them with the results presented in the referenced papers.

- **Data-Driven MPC for LTI systems:**

    The reproduction is implemented in [`robust_lti_dd_mpc_reproduction.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/lti_control/robust_lti_dd_mpc_reproduction.py). This script closely follows the example presented in **Section V of** [[1]](#1), which demonstrates various Robust Data-Driven MPC controller schemes applied to a four-tank system model.

    To run the script, execute the following command:
    ```bash
    python examples/lti_control/robust_lti_dd_mpc_reproduction.py
    ```

- **Data-Driven MPC for Nonlinear systems:**

    The reproduction is included in the example script [`nonlinear_dd_mpc_example.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/nonlinear_control/nonlinear_dd_mpc_example.py), which closely follows the example presented in **Section V of** [[2]](#2) for the control of a nonlinear continuous stirred tank reactor (CSTR) system.

    To run the script, execute the following command:
    ```bash
    python examples/nonlinear_control/nonlinear_dd_mpc_example.py --seed 0
    ```

The figures below show the expected output from executing these scripts. The graphs from our results closely resemble those shown in **Fig. 2 of** [[1]](#1) and **Fig. 2 of** [[2]](#2), with minor differences due to randomization.

|LTI Data-Driven MPC|Nonlinear Data-Driven MPC|
|-|-|
|<img src="https://raw.githubusercontent.com/pavelacamposp/direct-data-driven-mpc/main/docs/resources/robust_dd_mpc_reproduction.png" alt="Robust Data-Driven MPC Animation">|<img src="https://raw.githubusercontent.com/pavelacamposp/direct-data-driven-mpc/main/docs/resources/nonlinear_dd_mpc_reproduction.png" alt="Nonlinear Data-Driven MPC Animation">|
|Reproduction of results from [[1]](#1)|Reproduction of results from [[2]](#2)|

## Code Structure

### Direct Data-Driven MPC Controller
The project is structured as a Python package, encapsulating the core logic of the Data-Driven MPC controllers within the following modules:
- [`direct_data_driven_mpc/lti_data_driven_mpc_controller.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/direct_data_driven_mpc/lti_data_driven_mpc_controller.py): Implements a Data-Driven MPC controller for LTI systems in the `LTIDataDrivenMPCController` class. This implementation is based on the **Nominal and Robust Data-Driven MPC schemes** described in [[1]](#1).
- [`direct_data_driven_mpc/nonlinear_data_driven_mpc_controller.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/direct_data_driven_mpc/nonlinear_data_driven_mpc_controller.py): Implements a Data-Driven MPC controller for nonlinear systems in the `NonlinearDataDrivenMPCController` class. This implementation is based on the **Nonlinear Data-Driven MPC scheme** described in [[2]](#2).

The utility module [`direct_data_driven_mpc/utilities/hankel_matrix_utils.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/direct_data_driven_mpc/utilities/hankel_matrix_utils.py) is used for constructing Hankel matrices and evaluating whether data sequences are persistently exciting of a given order.

### Model Simulation
The following utility modules have been implemented to simulate LTI and nonlinear systems:
- [`direct_data_driven_mpc/utilities/models/lti_model.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/direct_data_driven_mpc/utilities/models/lti_model.py): Implements the `LTIModel` and `LTISystemModel` classes for simulating LTI systems.
- [`direct_data_driven_mpc/utilities/models/nonlinear_model.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/direct_data_driven_mpc/utilities/models/nonlinear_model.py): Implements the `NonlinearSystem` class for simulating nonlinear systems.

### Controller Creation
To modularize the creation of Data-Driven MPC controllers, the following utility modules are provided:
- [`direct_data_driven_mpc/utilities/controller/controller_creation.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/direct_data_driven_mpc/utilities/controller/controller_creation.py): Provides functions for creating Data-Driven MPC controller instances from specified configuration parameters for both LTI and nonlinear controllers.
- [`direct_data_driven_mpc/utilities/controller/controller_params.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/direct_data_driven_mpc/utilities/controller/controller_params.py): Provides functions for loading Data-Driven MPC controller parameters from YAML configuration files for both LTI and nonlinear controllers.
- [`direct_data_driven_mpc/utilities/controller/initial_data_generation.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/direct_data_driven_mpc/utilities/controller/initial_data_generation.py): Provides functions for generating input-output data from LTI and nonlinear systems, which can be used as initial trajectories in Data-Driven MPC controller creation.

### Data-Driven Controller Simulation
The [`direct_data_driven_mpc/utilities/controller/data_driven_mpc_sim.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/direct_data_driven_mpc/utilities/controller/data_driven_mpc_sim.py) module implements the main control loops for both Data-Driven MPC controllers, following **Algorithms 1 and 2 of** [[1]](#1) for LTI systems and **Algorithm 1 of** [[2]](#2) for nonlinear systems.

### Visualization (Static and Animated Plots)
Custom functions are provided in [`direct_data_driven_mpc/utilities/visualization/`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/direct_data_driven_mpc/utilities/visualization/) to display input-output data in static and animated plots. These functions use Matplotlib for visualization and FFmpeg for saving animations in various formats (e.g., GIF, MP4).

### Examples
The `examples` directory contains scripts that demonstrate the operation of the Data-Driven MPC controller and reproduce the results presented in the referenced papers.
- [`examples/lti_control/lti_dd_mpc_example.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/lti_control/lti_dd_mpc_example.py): Demonstrates the setup, simulation, and data visualization of a Data-Driven MPC controller applied to an LTI system.
- [`examples/lti_control/robust_lti_dd_mpc_reproduction.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/lti_control/robust_lti_dd_mpc_reproduction.py): Implements a reproduction of the example presented in [[1]](#1), showing various Robust Data-Driven MPC schemes applied to an LTI system.
- [`examples/nonlinear_control/nonlinear_dd_mpc_example.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/nonlinear_control/nonlinear_dd_mpc_example.py): Demonstrates the setup, simulation, and data visualization of a Data-Driven MPC controller applied to a nonlinear system while closely following the example presented in [[2]](#2).

### Configuration Files
The system and controller parameters used in the example scripts are defined in YAML configuration files in [`examples/config/`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/config/). These parameters are based on the examples from **Section V of** [[1]](#1) for LTI systems, and from **Section V of** [[2]](#2) for nonlinear systems.

- **Data-Driven MPC controllers:**
    - [`examples/config/controllers/lti_dd_mpc_example_params.yaml`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/config/controllers/lti_dd_mpc_example_params.yaml): Defines parameters for a Data-Driven MPC controller designed for LTI systems.
    - [`examples/config/controllers/nonlinear_dd_mpc_example_params.yaml`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/config/controllers/nonlinear_dd_mpc_example_params.yaml): Defines parameters for a Data-Driven MPC controller designed for nonlinear systems.
- **Models:**
    - [`examples/config/models/four_tank_system_params.yaml`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/config/models/four_tank_system_params.yaml): Defines system model parameters for a linearized version of a four-tank system.
    - [`examples/config/models/nonlinear_cstr_system_params.yaml`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/config/models/nonlinear_cstr_system_params.yaml): Defines system model parameters for a nonlinear continuous stirred tank reactor (CSTR) system.
- **Plots:**
    - [`examples/config/plots/plot_params.yaml`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/examples/config/plots/plot_params.yaml): Defines Matplotlib properties of lines, legends, and figures for input-output plots.

A YAML loading function is provided in  [`direct_data_driven_mpc/utilities/yaml_config_loading.py`](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/direct_data_driven_mpc/utilities/yaml_config_loading.py).

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/pavelacamposp/direct-data-driven-mpc/blob/main/LICENSE) file for details.

## Citation
If you use these controller implementations in your research, please cite the original papers:

### Data-Driven MPC Control for Linear Time-Invariant (LTI) systems
<a id="1">[1]</a>
J. Berberich, J. Köhler, M. A. Müller and F. Allgöwer, "Data-Driven Model Predictive Control With Stability and Robustness Guarantees," in IEEE Transactions on Automatic Control, vol. 66, no. 4, pp. 1702-1717, April 2021, doi: [10.1109/TAC.2020.3000182](https://doi.org/10.1109/TAC.2020.3000182).

#### BibTex entry:
```bibtex
@ARTICLE{9109670,
  author={Berberich, Julian and Köhler, Johannes and Müller, Matthias A. and Allgöwer, Frank},
  journal={IEEE Transactions on Automatic Control},
  title={Data-Driven Model Predictive Control With Stability and Robustness Guarantees},
  year={2021},
  volume={66},
  number={4},
  pages={1702-1717},
  doi={10.1109/TAC.2020.3000182}}
```

### Data-Driven MPC Control for Nonlinear systems
<a id="2">[2]</a>
J. Berberich, J. Köhler, M. A. Müller and F. Allgöwer, "Linear Tracking MPC for Nonlinear Systems—Part II: The Data-Driven Case," in IEEE Transactions on Automatic Control, vol. 67, no. 9, pp. 4406-4421, Sept. 2022, doi: [10.1109/TAC.2022.3166851](https://doi.org/10.1109/TAC.2022.3166851).

#### BibTex entry:
```bibtex
@ARTICLE{9756053,
  author={Berberich, Julian and Köhler, Johannes and Müller, Matthias A. and Allgöwer, Frank},
  journal={IEEE Transactions on Automatic Control},
  title={Linear Tracking MPC for Nonlinear Systems—Part II: The Data-Driven Case},
  year={2022},
  volume={67},
  number={9},
  pages={4406-4421},
  doi={10.1109/TAC.2022.3166851}}
```
