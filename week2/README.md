house price predictor using scikit-learn

this project builds a simple ML model (regression model) using scikit-learn. The goal is making a model who can predict price of any house given and the model is trained using some chosen features. and these key features are area, stories, parking, bathroom and airconditioning.

the work flow i followed : load data , understand and clean the data, select features, train a model and evalute the models performance


What the program does


Loads and inspects data


Reads the CSV into a pandas DataFrame, shows shape, example rows, and data types to understand the columns and spot issues.

Cleans the data


Removes duplicate rows and checks for missing values.


Inside the ML pipeline, numeric features are filled with their mean, and the categorical feature airconditioning is filled with the most frequent value, then one‑hot encoded.

Explores and selects features


Uses plots (distributions, scatter plots, boxplots, correlation heatmap) to visualize how each feature relates to price.
Based on these relationships it chooses the small feature set listed above.

Splits, trains, and evaluates

Splits the data into training and test sets (80/20).


Builds a pipeline that applies preprocessing and then LinearRegression.

Trains the model on the training set and evaluates on the test set using MAE, MSE, RMSE, and R² (about 0.66, meaning the model explains roughly two‑thirds of the variation in prices).

Visualises predictions

Draws a scatter plot of actual vs predicted prices with a diagonal “perfect prediction” line to visually check how close predictions are.
