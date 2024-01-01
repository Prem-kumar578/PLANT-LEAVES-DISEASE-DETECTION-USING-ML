    from sklearn.tree import DecisionTreeClassifier 
clf=DecisionTreeClassifier() 
clf.fit(x_train,y_train) 
y_pred=clf.predict(x_test) 

