# PyPSA H<sub>2</sub> Training

🎯 Welcome to the training repository for simple hydrogen model using PyPSA. 

## 🏗️ Installation

### Step 1: Setting up the environment

To create the environment, navigate to the folder `pypsa-h2-training` in your terminal (for windows find `Anaconda Prompt`, for linux and mac you can use the normal `terminal`) and run the following command:

```shell title="create environment locally"
conda env create -f env-local.yaml
```

### Step 2: Installing solver

Solver installation is dependent on the operating system you are using. Therefore, please follow the instructions based on your OS.

#### Windows

To installed solver in windows machine requires a bit indirect approach. Here we will put the solver file directly in our environment.

To do this, please downlaod the `cbc.exe` and `clp.exe` file from [here](https://cloud.sefep.eu/s/WbiXr7ksMddk2fz). Then you need copy this file into your conda environment. Specifically, you need to copy these file in `C:\Users\<YOUR USER NAME>\anaconda3\envs\pypsa-agora-h2\Library\bin`. This is the defualt location of the anaconda environment. Incase, you created your anaconda environment at some other location, you would have to copy it there.

#### Mac

The best way to install cbc is through [Homebrew](https://brew.sh/). If Homebrew is not installed:

```shell title="installation of cbc in Mac1"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After installing Homebrew, run in terminal:

```shell title="installation of cbc in Mac2"
brew install cbc
```

#### Linux / WSL (Windows Sub-System for Linux)

Activate the `pypsa-h2` environment with `conda activate pypsa-h2` and run in terminal the following command:

```shell title="installation of cbc in WSL"
conda install conda-forge::coincbc
```

> [!Note]
> If the environment installation doesn't work for you, you can use run the excercise online using [Binder](https://mybinder.org/) available [here](https://mybinder.org/v2/gh/agoenergy/pypsa-agora-h2-training/HEAD).

## 📚 Resources

- [Training Material incl. slides and datasets](https://cloud.sefep.eu/s/5tKc4Ddkm7sDNQQ?path=%2F)
- [PyPSA documentation](https://pypsa.readthedocs.io/en/latest/)
- [EU map of hydrogen production](https://www.agora-industry.org/data-tools/agoras-eu-map-of-hydrogen-production-costs)
- [9 Insights on Hydrogen - Souteast Asia Edition](https://www.agora-energiewende.org/publications/9-insights-on-hydrogen-southeast-asia-edition)
- [12 Insights on Hydrogen - Brazil Edition](https://www.agora-energiewende.org/publications/12-insights-on-hydrogen-brazil-edition-1)
- [PtX Business Opportunity Analyser](https://www.agora-industry.org/data-tools/ptx-business-opportunity-analyser)
