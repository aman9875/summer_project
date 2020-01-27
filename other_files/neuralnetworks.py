import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap
from sklearn.neural_network import MLPClassifier

from sklearn.datasets import make_classification

X,Y = make_classification(n_samples = 100, n_features=2,n_redundant=0, n_informative=2, n_clusters_per_class=1, flip_y = 0.1, class_sep = 0.5, random_state=0)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=0)
hidden_layer=[1,10,100]
alpha=[0.01,0.1,1,5]
print "Effect of changing the regularization parameter"	
for i in alpha:
	nncf=MLPClassifier(hidden_layer_sizes=[100,100],activation='tanh',alpha=i,solver='lbfgs',random_state=0).fit(X_train,Y_train)
	print nncf.score(X_train,Y_train)
	print nncf.score(X_test,Y_test)
	print "\n"

print "Effect of changing the number of hidden units"

for i in hidden_layer:
	nncf=MLPClassifier(hidden_layer_sizes=[i],activation='tanh',solver='lbfgs',alpha=1,random_state=0).fit(X_train,Y_train)
	print nncf.score(X_train,Y_train)
	print nncf.score(X_test,Y_test)
	print "\n"

plt.scatter(X[:, 0], X[:, 1], c=Y,marker= 'o', s=50)
plt.show()