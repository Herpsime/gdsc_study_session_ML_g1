Breast cancer detector using logistic regression


this project builds a simple ML model  using scikit-learn (logistic regression).

The goal is making a model who can predict if breast cancer is benign or malignant given cell biopsy measurements. and these key features are clump thickness, uniformity of cell size/shape, marginal adhesion, single epithelial cell size, bare nuclei, bland chromatin, normal nucleoli, and mitoses.

the work flow i followed : load data ,then set features and target,split the data into testing and trianing, clean the data,  train a model, evaluate the models performance, finally visualize

What the program does

Loads and inspects data

Reads the CSV into a pandas DataFrame, shows shape (699 samples), example rows, missing values marked as '?', and class distribution (458 benign, 241 malignant) to understand the medical biopsy features.

Explores and selects features, split

All 9 medical features are used as they're standard for cancer diagnosis. No reduction needed.

Splits data 70/30 with stratification to keep class balance.

Cleans the data

Converts '?' to NaN for missing values. Inside the ML pipeline, all numeric features use median imputation to handle missing biopsy data effectively.


trains, and evaluates


Builds pipeline: median imputation -> standard scaling -> LogisticRegression.

Trains on training set, evaluates on test set: 98.1% accuracy, confusion matrix shows 135/138 benign correct, 71/72 malignant correct (only 1 missed cancers, 3 false alarm).

Visualises predictions

Confusion matrix heatmap with color coding clearly shows true negatives (135), false positives (3), false negatives (1 missed cancers), true positives (71).
