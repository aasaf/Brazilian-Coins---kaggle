# Brazilian Coins


## Dataset
Download the dataset from Kaggle - https://www.kaggle.com/lgmoneda/br-coins
Extract 2 directories (classification_dataset and regression dataset) 
    (a) For input_classification_path 
    (b) For input_regression_path
    
## Create 2 empty directories for outputs -  
    (a) For classification model dataset (will be our <output_classification_path> for the classification model) 
    (b) For regression model dataset (will be our <output_path> for the regression model)
## Coins detection (for classification model) - 
    To create the dataset for our classifier model we need to detect exactly the coins in each image, crop them, and save them. 
    (a) Edit the file build_classification_dataset.py and change your input_classification_path and output_classification_path 
    (b) Run build_classification_dataset.py
