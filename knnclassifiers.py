import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

fruit=pd.read_table('fruits.txt')

lookup_fruit_name=dict(zip(fruit.fruit_label.unique(),fruit.fruit_name.unique()))

X=fruit[['mass','width','height']]
y=fruit['fruit_label']

X_train,X_test,y_train,y_test= train_test_split(X,y,random_state=0)
from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier(n_neighbors=1)

knn=knn.fit(X_train,y_train)
print knn.score(X_test,y_test)
fruit_prediction=knn.predict([[20,4.3,5.5]])
print lookup_fruit_name[fruit_prediction[0]]

print knn.predict(X_test)
