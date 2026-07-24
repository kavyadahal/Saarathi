# Linear regression :

```
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import \mean_squared_error , r2_score

model = LinearRegression()

x_train = np.array([
    [600],
    [750],
    [900],
    [1050],
    [1200],
    [1350],
    [1500],
    [1650],
    [1800],
    [1950],
    [2100],
    [2250],
    [2400],
    [2550],
    [2700]
])

# House price in thousands of dollars (Y)
y_train = np.array([
    120,
    145,
    170,
    190,
    215,
    240,
    265,
    285,
    310,
    335,
    360,
    385,
    405,
    430,
    455
])

y_test = np.array([285,
    310,
    335,
    360,
    385,
    405,
    430,
    455])
x_test = np.array([[1650],
    [1800],
    [1950],
    [2100],
    [2250],
    [2400],
    [2550],
    [2700]])

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
y_pred

rmse = np.sqrt(mean_squared_error(y_test,y_pred))
r2 = r2_score(y_test,y_pred)




```

![[Pasted image 20260723222443.png]]
![[Pasted image 20260723222358.png]]


# EXCERSICE 1:
-Load the built-in `diabetes` dataset (features → a number). - Split 80/20 with      `random_state=42`.
- `fit` a `LinearRegression`, `predict` on the test set.
- Print RMSE, MAE and R². Compare to a "predict the mean" baseline.


The `load_diabetes()` function returns a custom scikit-learn container object. This object acts like a Python dictionary. It holds multiple arrays and metadata inside specific attributes. [[1](https://towardsdatascience.com/json-and-apis-with-python-fba329ef6ef0/)]

```
       [ load_diabetes() Object ]
         ├── .data       ──> NumPy Array (442 x 10) [Features]
         ├── .target     ──> NumPy Array (442,)     [Labels]
         ├── .feature_names ──> List of 10 strings
         └── .DESCR      ──> Full text description
```


# Breast cancer:

Precision , recall &  F1:
True + True -ve 
False +ve False -ve

PRECISION :
TP/(TP+FP): Of everything you flagged positive , how much was right? Punishesh false alarms

RECALL:
TP / (TP+FN)

F1:
balance :
harmonic mean of the two . One number when you need a single score



```
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X ,y = load_breast_cancer(return_X_y = True) #features , labels

X_train , X_test , y_train , y_test = train_test_split(
    X , y , test_size = 0.2 , random_state=42 , stratify=y) 

#Stratify : Divide such that divides all features evenly

for depth in [1,3,5,None]:
    model = DecisionTreeClassifier(max_depth = depth , random_state = 42)
    model.fit(X_train,y_train)
    train = model.score(X_train,y_train)
    test = model.score(X_test,y_test)
    print(depth,round(train,3),round(test,3))
    



```

OUTPUT :

1 0.923 0.921
3 0.976 0.939  # Depth3 give much better ouput no over or underfitting.
5 0.993 0.921
None 1.0 0.912

# Cross validation score :

Completely removes luck from the equation : Stratified data model is obtained


