avg1=np.append(avgarray,avgarray1) 
avg2=np.append(avgarray2,avg1) 
avgall=avg2 
no_of_data=1200 
p=avgall; 
p=p.reshape(no_of_data,6); 
print(str(len(p))) 
df=pd.DataFrame(p) 
df.to_csv('f400n7.csv') 

