from sklearn.metrics import f1_score
from Linker import linker


# print_csv("C:\\Users\\Nikolas\\PycharmProjects\\Support_Vector_Machines\\Input\\winequality-red.csv")
# new_list = csv_to_1d_list("C:\\Users\\Nikolas\\PycharmProjects\\Support_Vector_Machines\\Input\\winequality-red.csv")
e = linker.csv_column_to_list("C:\\Users\\Nikolas\\PycharmProjects\\Support_Vector_Machines\\Input\\winequality-red.csv", 2)
print(e)

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 1, 2, 0, 1, 2]
print(f1_score(e, e, average='macro'))

