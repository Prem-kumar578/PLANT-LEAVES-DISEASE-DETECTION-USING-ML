from sklearn.linear_model import LogisticRegression 
model=LogisticRegression() 
model.fit(x_train,y_train) 
y_pred=model.predict(x_test) 

