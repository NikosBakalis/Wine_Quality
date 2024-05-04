# Wine Quality

## This is a project based on Suport Vector Machines (SVM)

### First step
This code will try to predict the quality of a wine.
Into the winequality-red.csv you can find wines each one with it's own specific characteristics.
One of them is the quality, given by the taster.
This file will be our training-test with analogy 75%-25% to mesure the performance of our model.
After we "train" our code we will try to predict the quality of a wine using Suport Vector Machines (SVM)
and we are going to mesure the outcome of the model using f1 score, precision and recall.

### Second step
The second part of the code will first remove the 33% of the items in the pH column.
After that, we have 4 different methods to handle the empty fields:
1. Empty the whole column.
2. Fill the columnt with the average of the remaining items.
3. Fill the column using Logistic-Regression.
4. Fill the column using K-means.
