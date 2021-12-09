import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

employee = pd.read_csv(r"C:\Users\mbcme\Documents\employee-numbers-only.csv")

X=employee.drop("LeaveOrNot", axis=1)

y=employee["LeaveOrNot"]

clf = RandomForestClassifier()

clf.get_params()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf.fit(X_train, y_train)

y_preds = clf.predict(X_test)

new_x= np.array([2,2017, 1, 3, 23, 1, 0, 0]).reshape(1,-1)

test_arr = [2,2017, 1, 3, 23, 1, 0, 0]

def predict_list(model_list):

    arr = np.array([model_list])
    arr.reshape((1, -1))
    result = clf.predict(arr)
    string1 = ''.join(str(e) for e in result)

    if string1 == "0":
        stay = "Employee will stay at company for the next 2 years."
        return stay
    leave = "Employee will leave the company in the next 2 years"
    return leave

predict_list(test_arr)






