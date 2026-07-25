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



```

# #Sometheory ----------------------------------------------

# #Theconfusionmatrix

- **TP / TN** — got it right (positive / negative).
- **FP** — false alarm. **FN** — missed it.
- Every classification metric is built from these four.

|   |   |   |
|---|---|---|
||Pred 0|Pred 1|
|Actual 0|TN 39|FP 3|
|Actual 1|FN 1|TP 71|

**FP vs FN is a real-world choice.** A missed cancer (FN) is far worse than a false alarm (FP). The matrix makes that trade-off visible.


![[Pasted image 20260726003236.png]]




![[Pasted image 20260726003427.png]]




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

--some features are genuinely useless noise, and feeding them to a model can hurt it. 
--**Feature selection** is the general idea of throwing away the useless columns before training. `SelectKBest` is one specific way to do that: score every column, then keep only the `k` highest-scoring ones.
--It needs a _scoring function_ to know what "best" means.`f_classif` is that scoring function.
This is literally called an F-statistic: `(how far apart the class averages are) ÷ (how spread out the values are within each class)`.


![[Pasted image 20260725230148.png]]
Okay, imagine a classroom quiz.

Your teacher wants to pick the **3 best study questions** to put on a practice test. But here's the sneaky mistake: she looks at **everyone's answers, including the kids who are supposed to take the test tomorrow**, and picks the questions that those exact kids already happened to get right. Then tomorrow, she gives those "best" questions as a surprise test... to the same kids whose answers she peeked at. Of course they do great! But it's not because the questions were actually good — it's because she cheated by looking at the answer sheet first.


```
from sklearn.linear_model import LogisiticRegression

from sklearn.feature_selection import SelectKBest , f_classif


```


# #Pipeline :


# Leaky order:

step 1 : SelectKBest.fit(X, y) — **every** patient, before any split exists
p3p4p6p2p1p5p7 ← peeked!p0 ← peeked!

step 2 : the split into train/test finally happens — but too late, the selector already used p7 and p0's labels
step 3 :  train and score the model — the "test" is no longer a fair, unseen test


```
X_sel = SelectKBest(f_classif , k=20).fit_transform(X,y) #leak!
leaky = cross_val_score(LogisticRegression(max_iter= 1000),X_sel,y,cv=5)
```

#  fit_transform` here means: _learn which 20 columns are best, using every single patient's label — then immediately reshape every single patient's row down to just those 20 columns, right now, in this one call_

--------------------------------------------------------------------------


# the pipeline's order of operations

step 1: split into train/test **first** — p7 and p0 are set aside, untouched

step 2 :  pipe.fit(X_train, y_train) — SelectKBest only ever calls .fit() on the 6 train patients

p3p4p6p2p1p5   p7 blocked p0 blocked

step 3 : pipe.score(X_test, y_test) — p7 and p0 are seen for the very first time here, only to grade the finished model

**`clf` is simply a **variable name** that stands for **classifier**

```
from sklearn.pipeline import pipeline
pipeline = Pipeline([
         ('select' , SelectKBest(k_classif , k = 20))
         ('clf' , LogisticRegression(max_iter = 1000))
])
honest = cross_val_score(pipe , X , y , cv = 5)
```
# print(leaky.mean(),honest.mean()) OUTPUT : #0.860 0.4