import pandas
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

df = pandas.read_csv("../Input/winequality-red.csv")
X_train, X_test, y_train, y_test = train_test_split(df[["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "sulphates", "alcohol", "quality"]], df.pH, test_size=0.25)

# print(X_train, X_test, y_train, y_test)
y_train_encoded = [round(x * 100) for x in y_train]
print(y_train, "\n", y_train_encoded)
given = [round(x * 100) for x in y_test]
print(y_test, "\n", given)

clf = SVC(gamma='auto')
clf.fit(X_train, y_train_encoded)
final = clf.predict(X_test)
print(final)

print(float(f1_score(given, final, average='micro')))
print(float(precision_score(given, final, average='micro')))
print(float(recall_score(given, final, average='micro')))
