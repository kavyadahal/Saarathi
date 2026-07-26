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



=---------------------------------------------------------------------------------------------------------
# Day 14 works: 

=-----------------------------------------------------------------------------------------------------------


Excersice 1 : 
Fit a DecisionTreeClassifier at depths 1, 2, 3, 5, and None.
Print train score and test score for each.
Watch the train score climb to 1.000 while the test score peaks and then falls.
Name the best depth — the one with the highest test score and smallest gap.


```
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score , train_test_split
from sklearn.tree import DecisionTreeClassifier

X,y = load_breast_cancer(return_X_y=True)
X_train , X_test , y_train , y_test = train_test_split(
    X , y , test_size = 0.2 , random_state=42 , stratify=y) 
    
for depth in [1,2,3,5,None]:
    model = DecisionTreeClassifier(max_depth=depth , random_state=42)
    model.fit(X_train,y_train)
    train = model.score(X_train,y_train)
    test = model.score(X_test,y_test)
    print(depth,round(train,3),round(test,3))

model.score(X_test, y_test)

from sklearn.feature_selection import SelectKBest , f_classif
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression


#Wrong: pick features using All the data then cross validate
X_select = SelectKBest(f_classif ,k = 20).fit_transform(X,y)
model = LogisticRegression(max_iter=5000)
leaky = cross_val_score(model , X_select , y , cv = 5)
#RIGHT : selection lives INSIDE THE PIPELINE , re-run per fold
pipe = Pipeline([
    ("select", SelectKBest(f_classif, k=20)),
    ("clf", LogisticRegression(max_iter=5000)),
])
honest = cross_val_score(pipe,X,y,cv =5)
print(leaky.mean(),honest.mean()) #0.860 0.415

#OUTPUT : 0.9490451793199813 0.9490451793199813


```
Exercise 2 — Cross-validate Run cross_val_score(model, X, y, cv=5) on the cancer data. Print the five fold scores. Print the mean and standard deviation. Report the result as mean ± std.

```
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

X , y = load_breast_cancer(return_X_y=True)
model = LogisticRegression(max_iter=5000)
score = cross_val_score(model , X , y , cv = 5)
print(score.mean())
print(score.std())

""" OUTPIUT: 
0.9507995652848935
0.01804054330253301"""
```

Exercise 3 — Catch the leak Build pure-noise data: random features, random labels. Leaky: select features on all data, then cross-validate. See the inflated score. Honest: put selection inside a Pipeline, cross-validate. See ~0.50. Sit with the gap. That gap is a career's worth of avoided disasters.

```
# Data: 
import numpy as np
import pandas as pd

# Step 1: set a seed so results are reproducible
np.random.seed(42)

# Step 2: decide the shape of the data
n_samples = 1000     # number of rows
n_features = 20       # number of columns

# Step 3: create random features
# Each value is drawn from a standard normal distribution (mean 0, std 1)
X = np.random.randn(n_samples, n_features)

# Step 4: create random labels
# For binary classification: random 0s and 1s
y = np.random.randint(0, 2, size=n_samples)

# Step 5: put it in a DataFrame so it's easy to inspect
feature_names = [f"feature_{i}" for i in range(n_features)]

# Create features and labels
df = pd.DataFrame(X, columns=feature_names)
df["label"] = y

from sklearn.feature_selection import SelectKBest , f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

model = LogisticRegression(max_iter=5000)

X_x = SelectKBest(f_classif,k = 10).fit_transform(X,y)
leak =cross_val_score(model , X_x , y , cv = 5) #leak

from sklearn.pipeline import Pipeline


pipe = Pipeline([
    ('select',SelectKBest(f_classif,k = 10)),
    ('clf',model)
])
honest = cross_val_score(pipe , X , y , cv =5)

print(leak.mean(),honest.mean()) #0.5309999999999999 0.514



```