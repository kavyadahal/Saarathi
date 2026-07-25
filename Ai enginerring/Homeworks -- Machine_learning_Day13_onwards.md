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

# EXCERSICE 2: 

- Load `breast_cancer` (features → malignant/benign).
- Split with `stratify=y`, fit a `LogisticRegression`.
- Print the confusion matrix.
- Print accuracy, precision, recall, F1 — and read them out loud.

```

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

X ,y = load_breast_cancer(return_X_y = True) #features , labels

X_train , X_test , y_train , y_test = train_test_split(
    X , y , test_size = 0.2 , random_state=42 , stratify=y) #Stratify : Divide such that divides all features evenly
    
model = LogisticRegression(max_iter = 5000)
model.fit(X_train , y_train)
pred = model.predict(X_test)

#Print the confusion matrix.
conf = confusion_matrix(y_test , pred)
print(conf)
```

OUTPUT : 
[[39  3]
 [ 1 71]]



# Exercise 3 · buffer / stretch

## Prove that accuracy lies : - 
-  Build a fake imbalanced set: 980 negatives, 20 positives.
- Make a "model" that always predicts 0.
- Print its accuracy, recall and precision — watch accuracy say 0.98 while recall says 0.00.

```
#Creation of imbalanced set
#Build a fake imbalanced set: 980 negatives, 20 positives.
import numpy as np
import pandas as pd
n_neg = 980
n_pos = 20
np.random.seed(42)
neg_x1 = np.random.normal(loc=0, scale=1.5, size=n_neg)
neg_x2 = np.random.normal(loc=0, scale=1.5, size=n_neg)

pos_x1 = np.random.normal(loc=0.8, scale=1.5, size=n_pos)
pos_x2 = np.random.normal(loc=0.8, scale=1.5, size=n_pos)

#Two features: 
X1 = np.concatenate([neg_x1, pos_x1])
X2 = np.concatenate([neg_x2, pos_x2])
#Label:take the list [0] and repeat it 980
y = np.array([0]*n_neg + [1]*n_pos)
#[980 zeros]  +  [20 ones]  =  [980 zeros, then 20 ones]  (1000 items total)

df = pd.DataFrame({"feature_1": X1, "feature_2": X2, "label": y})
df = df.sample(frac=1, random_state=42).reset_index(drop=True)  # shuffle

df["label"].value_counts()

X = df[["feature_1","feature_2"]]
y = df["label"]

#Make a "model" that always predicts 0.
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , precision_score , recall_score

X_train , X_test , y_train , y_test = train_test_split(
    X , y , test_size=0.2 ,random_state=42 , stratify=y
)
model = LogisticRegression(max_iter=5000)
model.fit(X_train , y_train)
pred = model.predict(X_test)

acc = accuracy_score(y_test , pred)
prec = precision_score(y_test , pred)
recall = recall_score(y_test , pred)
print(acc , prec , recall)
print(y_test.value_counts())

print(np.unique(pred, return_counts=True))

#We can fix this by using 
#LogisticRegression(max_iter=5000, class_weight="balanced")

```
OUTPUT:

0.98 0.0 0.0
label
0    196
1      4
Name: count, dtype: int64
(array([0]), array([200]))


![[Pasted image 20260726011407.png]]

|Model|How it handles the rare 20|Good for you?|
|---|---|---|
|Logistic regression (no weighting)|Ignores rare class, predicts "normal" always|❌ trap — 98% accuracy, 0 spam caught|
|Logistic regression + `class_weight="balanced"`|Forces itself to pay more attention to spam|✅ okay baseline|
|Random forest + `class_weight="balanced"`|Builds many small decision trees, votes — handles messy/non-straight-line patterns better|✅ usually stronger than logistic|
|Random forest / XGBoost + oversampling (SMOTE)|First _creates fake extra spam examples_ to balance the training data, then trains|✅✅ often the best for very rare classes like 20 out of 1000|
|Isolation Forest / anomaly detection|Doesn't learn "spam vs normal" — instead learns "what does normal look like" and flags anything weird|✅ good when spam is very rare and looks totally different from normal|
# class_weight="balanced" = pay more attention to the rare 20 spam rows if we use this in model()


