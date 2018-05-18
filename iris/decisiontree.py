import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import graphviz

balance_data = pd.read_csv('iris.csv',sep= ',', header= None)

X = balance_data.values[:, 0:4]
Y = balance_data.values[:,4]

X_train, X_test, y_train, y_test = train_test_split( X,
                                                     Y,
                                                     test_size = 0.4,
                                                     random_state = 100)

clf_entropy = DecisionTreeClassifier(criterion = "entropy",
                                     random_state = 100)
clf_entropy.fit(X_train, y_train)

y_pred_en = clf_entropy.predict(X_test)

for i in range(len(X_test)):
    print X_test[i], "--> fakta: ", y_test[i], "; prediksi: ", y_pred_en[i]

print "Accuracy is ", accuracy_score(y_test,y_pred_en)*100

dot_data=tree.export_graphviz(clf_entropy)
graph = graphviz.Source(dot_data)
graph.render("iris.pdf")

