# Residence time of 1,2,4-triazole  in Lake Geneva

## Repository Information

This repository provides the data and scripts to run a two-box  model estimating the residence time of 1,2,4-triazole in Lake Geneva with different mixing scenarios.

Link to the GitHub repository: https://github.com/tdoda/triazole-Geneva.git

## Installation (TO UPDATE)

### 1. Python installation

Python 3 is required to run the scripts. Three installation are possible:
- Recommended option: download [Miniforge](https://github.com/conda-forge/miniforge). 
- User-friendly option: download the [Anaconda distribution](https://www.anaconda.com/products/individual).
- Classic option: download Python from the [official website](https://www.python.org/downloads/).

### 2. Repository installation

- If using GIT, clone the repository to your local machine using the command in Git Bash: 

    ``` 
    git clone https://github.com/tdoda/triazole-Geneva.git 
    ```
 
    Note that the repository will be copied to your current working directory.
- Without GIT, just download the entire ZIP folder from https://github.com/tdoda/triazole-Geneva.git ("Code" > "Download ZIP") and extract it.

### 3. Packages installation

1. Open the terminal (e.g., Anaconda Prompt), and move to the `triazole-Geneva` repository.
2. Create a new environment *triazole-Geneva* and install the packages as follows:
    - If using conda (Anaconda or Miniforge installation):
        ```
        conda env create -f environment.yml
        conda activate triazole-Geneva
        ```
        It is also possible to install the packages from `requirements.txt` with pip instead:
        ```
        conda create -n triazole-Geneva python=3.12
        conda activate triazole-Geneva
        pip install -r requirements.txt
        ```
    - If using mamba (Anaconda or Miniforge installation):
        ```
        mamba env create -f environment.yml
        mamba activate triazole-Geneva 
        ```
    - If using pip (classic Python installation):
        ```
        python -m venv triazole-Geneva       
        source triazole-Geneva /bin/activate  # For Linux/macOS
        triazole-Geneva\Scripts\activate     # For Windows
        pip install -r requirements.txt
        ```


## Usage

How to run the model

## Organization of the repository

### Overview of the repository structure

    triazole-Geneva/
    ├── data/ 
    ├── mixing_depth/
    │   └── historical_deep_mixing.csv
    ├── morphology/
    │   └── Lake_Geneva_Morphology.csv
    └──plunge_depth/
    │   └── plunge_depth_percentage.csv
    ├── figures/ 
    ├── notebooks/
    │   ├── Model_analytical/
    │   └── Model_varying_mixing/
    │       ├── Mixing_simulation/
    │       ├── Results/
    │       └── Figures/
    ├── report/
    ├── requirements.txt 
    ├── environment.yml 
    └── README.md 

### Folder `data`

### Folder `notebooks`

### Folder `figures`

### Folder `report`

## Contact information