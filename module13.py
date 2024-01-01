from sklearn.naive_bayes import GaussianNB 
classifier=GaussianNB() 
classifier.fit(x_train,y_train) 
y_pred=classifier.predict(x_test) 

