import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
#from sklearn.datasets import make_classification, make_blobs
from matplotlib.colors import ListedColormap
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
X,Y=make_regression(n_samples=100,n_features=1,n_informative=1,bias=150.0,noise=30,random_state=0)
poly=PolynomialFeatures(degree=2)

X=poly.fit_transform(X)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=0)

scaler=MinMaxScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

linreg=Ridge(alpha=2.0).fit(X_train_scaled,Y_train)

print linreg.coef_
print linreg.intercept_
print linreg.score(X_train_scaled,Y_train)
print linreg.score(X_test_scaled,Y_test)

'''
plt.figure()
plt.title("sample regression dataset")
plt.scatter(X,Y,marker='o',s=50)
plt.show()
'''               