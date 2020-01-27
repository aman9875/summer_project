import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification,make_blobs
from matplotlib.colors import ListedColormap

X,Y = make_classification(n_samples = 100, n_features=2,n_redundant=0, n_informative=2, n_clusters_per_class=1, flip_y = 0.1, class_sep = 0.5, random_state=0)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=0)
log=LogisticRegression(C=1).fit(X_train,Y_train)

print log.intercept_
print log.coef_
print log.score(X_train,Y_train)
print log.score(X_test,Y_test)

plt.scatter(X[:, 0], X[:, 1], c=Y,marker= 'o', s=50)
plt.show()



                          
