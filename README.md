# ASAD_DenseNet Project

### Introduction
This project implements **ASAD_DenseNet**, and contains the code necessary to reproduce the results from the paper:  
> **ICASSP 2024 Accepted Paper** - You can access the paper here: [ICASSP 2024 Paper](https://ieeexplore.ieee.org/document/10448013)

### Project Structure

1. **1_download_data**  
   - Contains `download_data.py` to easily retrieve the raw EEG dataset.  
   - Dataset used: **KUL dataset**, which can be downloaded from [Zenodo](https://zenodo.org/records/4004271).  
   - The data will be downloaded to the `../2_data` folder for further processing.

2. **2_data**  
   - This folder is where all the downloaded data will be stored (e.g., `S1.mat` to `S16.mat`).  
   - Currently, it’s empty but will be filled after running the data download script.

3. **3_preprocess**  
   - This folder contains files for preprocessing the EEG data.  
   - Notable files:
     - `EEG_2D.xlsx`: Contains the spatial arrangement of EEG electrodes.
     - `EEG_map.mat`: Labels of electrodes (1-64).
     - `preprocess.m`: Requires **MATLAB** and the **EEGLAB toolbox**, which you can download [here](https://sccn.ucsd.edu/eeglab/download.php).  
   - After running the `preprocess_IIR.m` script, the `4_processed_data` folder will be populated.

4. **4_processed_data**  
   - This folder stores processed data files (`KUL_1D.mat` and `KUL_2D.mat`).  
   - These files are required for model training and analysis.

5. **5_train_and_test_model**  
   - Contains code to train and test the models (divided into sections 4.1 and 4.2 of the paper).  
   - The process is divided into **five-fold cross-validation** to ensure no data leakage.  
   - Files:
     - `main.py`: Handles data splits.
     - `train_valid_and_test.py`: Manages training, validation, and testing.  
     - `AADdataset.py`: Creates the dataset for the model.
