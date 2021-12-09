import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

employee = pd.read_csv(r"C:\Users\mbcme\Documents\employee-numbers-only.csv")

print(employee.head())

X=employee.drop("LeaveOrNot", axis=1)

y=employee["LeaveOrNot"]

clf = RandomForestClassifier()

clf.get_params()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf.fit(X_train, y_train)

y_preds = clf.predict(X_test)

new_x= np.array([2,2017, 1, 3, 23, 1, 0, 0]).reshape(1,-1)
print(clf.predict(new_x))


def predict_list(model_list):
    list = np.array(model_list)
    list.reshape((1, -1))
    result = clf.predict(list)
    print(clf.predict(list))

    return result









