from sklearn.svm import SVC 
from sklearn import svm,datasets 
from sklearn import model_selection 
import pickle 
svm=SVC(kernel='linear',probability=True,random_state=42) 
svm.fit(x_train,y_train) 
y_pred=svm.predict(x_test) 

