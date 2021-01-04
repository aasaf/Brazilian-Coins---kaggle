
1) Download the dataset from kaggle link  - https://www.kaggle.com/lgmoneda/br-coins
2) Extract 2 directories (classification_dataset and regression dataset)
    (a) For input_classification_path
    (b) For input_regression_path
3) Create 2 empty directories for outputs:
    (a) For classification model dataset (will be our <output_classification_path> for the classification model)
    (b) For regression model dataset (will be out <output_path> for the regression model)
4) For create the dataset for our classifier model we need to detect exactly the coins each image, crop them and save.
    (a) Edit the file build_classification_dataset.py and change your input_classification_path and output_classification_path
    (b) Run build_classification_dataset.py
5)
