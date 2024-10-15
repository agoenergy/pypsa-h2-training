# pypsa-agora-h2-training

# Installation

## Step 1: Setting up the environment

To create the environment, navigate to the folder `pypsa-agora-h2-training` in your terminal and run the following command:

```
conda env create -f environment.yaml
```

## Step 2: Installing solver 

### Windows
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
