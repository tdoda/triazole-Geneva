# Residence time of 1,2,4-triazole  in Lake Geneva

## Repository Information

This repository provides the data and scripts to run a two-box  model estimating the residence time of 1,2,4-triazole in Lake Geneva with different mixing scenarios.

Link to the GitHub repository: https://github.com/tdoda/triazole-Geneva.git

## Installation (TO UPDATE)

### 1. Python installation

Python 3 (version > 3.11) is required to run the scripts. Three installation are possible:
- Recommended option: download [Miniforge](https://github.com/conda-forge/miniforge). 
- User-friendly option: download the [Anaconda distribution](https://www.anaconda.com/products/individual).
- Classic option: download Python from the [official website](https://www.python.org/downloads/).

### 2. Repository installation

- If using GIT, clone the repository to your local machine using the command in Git Bash: 

    ``` 
    git clone https://github.com/tdoda/lake-kivu-ctd-database.git 
    ```
 
    Note that the repository will be copied to your current working directory.
- Without GIT, just download the entire ZIP folder from https://github.com/tdoda/lake-kivu-ctd-database.git ("Code" > "Download ZIP") and extract it.

### 3. Packages installation

1. Open the terminal (e.g., Anaconda Prompt), and move to the `lake-kivu-ctd-database` repository.
2. Create a new environment *kivu-ctd* and install the packages as follows:
    - If using conda (Anaconda or Miniforge installation):
        ```
        conda env create -f environment.yml
        conda activate kivu-ctd 
        ```
        It is also possible to install the packages from `requirements.txt` with pip instead:
        ```
        conda create -n kivu-ctd python=3.11
        conda activate kivu-ctd
        pip install -r requirements.txt
        ```
    - If using mamba (Anaconda or Miniforge installation):
        ```
        mamba env create -f environment.yml
        mamba activate kivu-ctd 
        ```
    - If using pip (classic Python installation):
        ```
        python -m venv kivu-ctd       
        source kivu-ctd /bin/activate  # For Linux/macOS
        kivu-ctd\Scripts\activate     # For Windows
        pip install -r requirements.txt


## Usage

How to run the model

## Organization of the repository

### Overview of the repository structure

### Folder `data`

## Contact information