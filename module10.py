   from sklearn.neighbors import KNeighborsClassifier 
knn=KNeighborsClassifier(n_neighbors=14) 
knn.fit(x_train,y_train)

y_pred=knn.predict(x_test) 

