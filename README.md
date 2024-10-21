# PyPSA-Agora Hydrogen Training 

🎯 Welcome to the training repository for simple hydrogen model using PyPSA. 

# 🏗️ Installation

## Step 1: Setting up the environment

To create the environment, navigate to the folder `pypsa-agora-h2-training` in your terminal and run the following command:

```
conda env create -f env-local.yaml
```

## Step 2: Installing solver
Solver installation is dependent on the operating system you are using. Therefore, please follow the instructions based on your OS. 

### Windows
To installed solver in windows machine requires a bit indirect approach. Here we will put the solver file directly in our environment. 

To do this, please downlaod the `cbc.exe` and `clp.exe` file from here. Then you need copy this file into your conda environment. Specifically, you need to copy these file in `C:\Users\<YOUR USER NAME>\anaconda3\envs\pypsa-agora-h2\Library\bin`. This is the defualt location of the anaconda environment. Incase, you created your anaconda environment at some other location, you would have to copy it there. 

### Mac

The best way to install cbc is through [Homebrew](https://brew.sh/). If Homebrew is not installed:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
After installing Homebrew, run in terminal:
```
brew install cbc
```

### Linux / WSL (Windows Sub-System for Linux) 

Activate the `pypsa-agora-h2` environment with `conda activate pypsa-agora-h2` and run in terminal the following command:

```
conda install conda-forge::coincbc
```

> [!Note]
> If the environment installation doesn't work for you, you can use run the excercise online using [Binder](https://mybinder.org/) available [here](https://mybinder.org/v2/gh/agoenergy/pypsa-agora-h2-training/HEAD).

# 📚 Resources
- [PyPSA documentation](https://pypsa.readthedocs.io/en/latest/)
- [EU map of hydrogen production](https://www.agora-industry.org/data-tools/agoras-eu-map-of-hydrogen-production-costs)
- [9 Insights on Hydrogen - Souteast Asia Edition](https://www.agora-industry.org/data-tools/agoras-eu-map-of-hydrogen-production-costs) 
- [12 Insights on Hydrogen - Brazil Edition](https://www.agora-industry.org/data-tools/agoras-eu-map-of-hydrogen-production-costs) 
- [PtX Business Opportunity Analyser](https://www.agora-industry.org/data-tools/agoras-eu-map-of-hydrogen-production-costs)

