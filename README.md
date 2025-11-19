<!--
-*- coding: utf-8 -*-
SPDX-FileCopyrightText: 2025 PyPSA-H2-Training Developers
SPDX-License-Identifier: GPL-2.0-or-later
-->

# PyPSA H₂ Training

🎯 Welcome to the training repository for simple hydrogen model using PyPSA. 

## 🏗️ Installation

### Step 1: Clone the Repository

First, clone the [PyPSA H₂ Training repository](https://github.com/agoenergy/pypsa-h2-training) using the **Git** version control system. **Important:** the path to the directory where the repository is cloned **must not contain any spaces**.

If Git is not installed on your system, please follow the [Git installation instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

```shell title="Cloning the repository"
git clone https://github.com/agoenergy/pypsa-h2-training.git
cd pypsa-h2-training
```

### Step 2: Install the environment

To create the environment, we recommend using **Conda**, a package and environment management system, to handle these dependencies.

Start by installing [Miniconda](https://docs.conda.io/en/latest/miniconda.html), a lightweight version of [Anaconda](https://www.anaconda.com/) that includes only Conda and its core dependencies. If you already have Conda installed, you can skip this step. For installation instructions tailored to your operating system, refer to the [official Conda installation guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/).

The required Python packages for the exercises are listed in the `environment.yaml` file (which is called `pypsa-h2-training`) using the following commands in your terminal (for windows find `Anaconda Prompt`, for linux and mac you can use the normal `terminal`):

```shell title="Installing and activating the virtual environment"
conda env create -f environment.yml
conda activate pypsa-h2-training
```

### Step 3: Install a solver

The exercises in this repo is passed to an external solver to perform total annual system cost minimisation and obtain optimal power flows. PyPSA is compatible with several solvers that can be installed via Python.

**By default of the latest PyPSA version already installed some common open-source solvers like Cbc or HiGHs.** Therefore, after you activate the environment in this repository, you don't need to installed HiGHs or cbc solver manually. We use [HiGHs](https://ergo-code.github.io/HiGHS/dev/interfaces/python/) as the default solver of this repository and all exercises in the repository can be solved via this solver.

## Solver testing

After all the aboved installation steps are completed, you can try to run some testings to make sure that you get all packages installed correctly:

1. To test your installed solver, you can change the `solver` variable inside `test/test_solver.py` (by default `solver="highs"`). And then in your terminal (with environment activated), run the command below. If the message shows `SOLVER TESTING RESULTS: {YOUR_SOLVER_NAME} solved the network successfully.`, then the solve testing is passed!

```shell title="solver testing"
python test/test_solver.py
```

## 📚 Resources

- [Training Material incl. slides and datasets]()
- [PyPSA documentation](https://pypsa.readthedocs.io/en/latest/)
- [EU map of hydrogen production](https://www.agora-industry.org/data-tools/agoras-eu-map-of-hydrogen-production-costs)
- [9 Insights on Hydrogen - Souteast Asia Edition](https://www.agora-energiewende.org/publications/9-insights-on-hydrogen-southeast-asia-edition)
- [12 Insights on Hydrogen - Brazil Edition](https://www.agora-energiewende.org/publications/12-insights-on-hydrogen-brazil-edition-1)
- [PtX Business Opportunity Analyser](https://www.agora-industry.org/data-tools/ptx-business-opportunity-analyser)
