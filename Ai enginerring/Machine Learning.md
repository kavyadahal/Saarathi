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
mae = mean_absol 




```

![[Pasted image 20260723222443.png]]
![[Pasted image 20260723222358.png]]


# EXCERSICE 1:


-Load the built-in `diabetes` dataset (features → a number). - Split 80/20 with      `random_state=42`.
- `fit` a `LinearRegression`, `predict` on the test set.
- Print RMSE, MAE and R². Compare to a "predict the mean" baseline.


```
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.metrices import(
r2_score,
mean_squared_error,
mean_absolute_error
)

load_diabetes(return_X_y = True)

X_train , X_test , y_triain , y_test = train_test_split(
    X , y , test_size = 0.2 , random_state = 42
)
model = LinearRegression
model.fit(X_train , y_train)
pred = model.predict(X_test)

		


```
```
Esma training garayo : 

X_train , y_train : data(features) , label using model.fit(X_train , y_train)

prediction for X_test data : Its output is a label( ie Y_test ) using pred = model.predict(X_test)

Now check how much they match (the whole data using R2 , rmse , mae )

r2  = r2.score(pred,y_test)
rmse = np.sqrt(mean_squared_error(y_test,pred))
```







# BREAST CANCER:


# Decision Tree
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



```
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection imoort cross_val_score

X, y = load_breast_cancer(return_X_y = True)

model = LogisticRegression(max_iters = 5000)
scores = cross_val_score(model,X,y,cv=5)
print(scores)
print(scores.mean())
print(scores.std())


```

# SelectKBest and f_classif:


![[Pasted image 20260725182126.png]]Okay, imagine a classroom quiz.

Your teacher wants to pick the **3 best study questions** to put on a practice test. But here's the sneaky mistake: she looks at **everyone's answers, including the kids who are supposed to take the test tomorrow**, and picks the questions that those exact kids already happened to get right. Then tomorrow, she gives those "best" questions as a surprise test... to the same kids whose answers she peeked at. Of course they do great! But it's not because the questions were actually good — it's because she cheated by looking at the answer sheet first.


```
from sklearn.linear_model import LogisiticRegression
from sklearn.pipeline import pipeline
from sklearn.feature_selection import SelectKBest , f_classif



```


