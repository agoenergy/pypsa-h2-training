# pypsa-agora-h2-training

# Installation

## Step 1: Setting up the environment

To create the environment, navigate to the folder `pypsa-agora-h2-training` in your terminal and run the following command:

```
conda env create -f environment.yaml
```

## Step 2: Installing solver 

### Windows
To installed solver in windows machine requires a bit indirect approach. Here we will put the solver file directly in our environment. 

To do this, please downlaod the `cbc.exe` and `clp.exe` file from here. Then you need copy this file into your conda environment. Specifically, you need to copy these file in `C:\Users\<YOUR USER NAME>\anaconda3\envs\pypsa-agora-h2\Library\bin`. This is the defualt location of the anaconda environment. Incase, you created your anaconda environment at some other location, you would have to copy it there. 

### Mac

<!-- ```
$ sudo xcodebuild -license accept
$ brew tap coin-or-tools/coinor
$ brew install coin-or-tools/coinor/cbc
``` -->

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

# Resources
