import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_scor

# import data
data = pd.read_csv('Singapore.csv')
data.columns
clean_data = data.loc[:, ['Daily Rainfall Total (mm)', 'Mean Temperature (C)',
       'Dengue (Count)']]
clean_data.columns = ['rainfall', 'temp', 'dengue']
clean_data.describe()

# labelling the clean data
# let's say we take those above the 75th percentile to be an outbreak
# this means that as long as dengue > 307, it's considered an outbreak
labels = np.where(clean_data.loc[:, 'dengue'] > 307, 1, 0)
labels = list(labels)
clean_data['label'] = labels

# import sklearn to split dataset
from sklearn.model_selection import train_test_split

X = clean_data.loc[:, ['rainfall', 'temp']]
y = clean_data.loc[:, 'label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle = False)

## k - Nearest Neighbors

knn_model = KNeighborsClassifier(n_neighbors = 14) 
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)

# Evaluation
accuracy_score(y_test, y_pred_knn)
precision_score(y_test, y_pred_knn)
recall_score(y_test, y_pred_knn)

## Logistic Regression
from sklearn.linear_model import LogisticRegression

logreg_model = LogisticRegression()
logreg_model.fit(X_train, y_train)
y_pred_logreg = logreg_model.predict(X_test)

# Evaluation
accuracy_score(y_test, y_pred_logreg)
precision_score(y_test, y_pred_logreg)
recall_score(y_test, y_pred_logreg)

## Decision Tree
from sklearn.tree import DecisionTreeClassifier

tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)
y_pred_tree = tree_model.predict(X_test)

# Evaluation
accuracy_score(y_test, y_pred_tree)
precision_score(y_test, y_pred_tree)
recall_score(y_test, y_pred_tree)

## XGBoost
import xgboost as xgb
xgb_train = xgb.DMatrix(X_train, label = y_train)
xgb_test = xgb.DMatrix(X_test, label = y_test)

param = {'eta': 0.45,
         'max_depth': 15,
         'objective': 'binary:logistic'
         }

xgb_model = xgb.train(param, xgb_train, num_boost_round = 15)
y_pred_xgb = xgb_model.predict(xgb_test)
y_pred_xgb = np.where(np.array(y_pred_xgb) > 0.5, 1, 0)

# Evaluation
accuracy_score(y_test, y_pred_xgb)
precision_score(y_test, y_pred_xgb)
recall_score(y_test, y_pred_xgb)





