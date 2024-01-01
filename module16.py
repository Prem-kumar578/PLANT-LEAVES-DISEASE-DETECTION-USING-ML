from tkinter import *
 
import tkinter as tk 
from tkinter import filedialog 
from tkinter.filedialog import askopenfile 
from PIL import Image,ImageTk 
import tkinter as tk 
from tkinter import * 
from PIL import ImageTk, Image 
from tkinter import filedialog 
from tkinter.font import Font 
import os 
my_w=tk.Tk() 
my_w.geometry("500x500") 
my_w.title("Plant Disease Detection.com") 
my_font1=('times',18,'bold') 
l1=tk.Label(my_w,text='Upload Image',width=30,font=my_font1) l1.grid(row=1,column=1) 
b1 = tk.Button(my_w, text='Upload Image',  
width=20,command = lambda:upload_file()) 
b1.grid(row=5,column=1)  

def upload_file(): 
 global img 
 f_types = [('Jpg Files', '*.jpg')] 
 filename = filedialog.askopenfilename(filetypes=f_types)  global x
 
 x=filename 
 img = ImageTk.PhotoImage(file=filename) 
 # canvas.create_image(20,20,anchor=NW,image=img) 
 #ImageTk.PhotoImage(Image.open("img")) 
 #global b2 
 b2 =tk.Button(my_w,image=img) # using Button  
 #ImageTk.PhotoImage(Image.open("image"))  
 b2.grid(row=3,column=1) 
def Submit(): 
 import cv2 
 #global img 
 img=Image.open(x) 
 import numpy as np 
 a=np.array(img) 
 orig=a 
 gray=cv2.cvtColor(orig,cv2.COLOR_RGB2GRAY) 
 gray.shape 
 #plt.imshow(cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)) 
 img=gray 
 gray[0] 
 thresh = cv2.threshold(img,np.mean(img) , 255, cv2.THRESH_BINARY_INV)[-1]  cv2.imshow('thresholded',thresh) 
 cv2.waitKey(0) 
 cv2.destroyAllWindows()
 
 img=thresh 
 edges =cv2.dilate(cv2.Canny(img, 0, 255), None)  
 img=cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB) 
 cv2.imshow('edgedetection',img) 
 cv2.waitKey(0) 
 cv2.destroyAllWindows() 
 cnt=sorted(cv2.findContours(edges, cv2.RETR_LIST,  
cv2.CHAIN_APPROX_SIMPLE)[-2], key=cv2.contourArea)[-1]  mask = np.zeros((256,256), np.uint8) 
 masked=(cv2.drawContours(mask, [cnt],-1, 255, -1)) 
 dst= cv2.bitwise_and(orig, orig, mask=mask) 
 segmented=(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)) 
 # plt.imshow(masked, cmap='gray') 
 k=cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB) 
 cv2.imshow('Background removed',k) 
 cv2.waitKey(0) 
 cv2.destroyAllWindows() 
 clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8)) 
 lab = cv2.cvtColor(k, cv2.COLOR_BGR2LAB) # convert from BGR to LAB color  space 
 l, a, b = cv2.split(lab) # split on 3 different channels 
 l2 = clahe.apply(l) # apply CLAHE to the L-channel 
 lab = cv2.merge((l2,a,b)) # merge channels 
 img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR) # convert from LAB to BGR  cv2.imshow('Increased contrast', img2)
 
 cv2.waitKey(0) 
 cv2.destroyAllWindows() 
 image = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) 
 plt.imshow(image) 
 pixel_vals = image.reshape((-1,3)) 
 import cv2 
 from skimage import color 
 from skimage import io 
 pixel_vals = np.float32(pixel_vals) 
 criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)  k = 2 
 retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 1,  cv2.KMEANS_RANDOM_CENTERS) 
 centers = np.uint8(centers) 
 segmented_data = centers[labels.flatten()] 
 segmented_image= segmented_data.reshape((image.shape)) 
 window_name='Segmented Image' 
 cv2.imshow(window_name,segmented_image) 
 aa=segmented_image 
 cv2.waitKey(0) 
 cv2.destroyAllWindows() 
 import matplotlib.pyplot as plt 
 from skimage.feature import greycomatrix,greycoprops 
 from statistics import stdev 
 from fractions import Fraction as fr

 import statistics 
 from scipy.stats import entropy 
 from skimage import data 
 from skimage.util import img_as_ubyte 
 from skimage.filters.rank import entropy 
 from skimage.morphology import disk 
 import pickle 
 z=aa[:,:,0]; 
 glcm=greycomatrix(z,[5],[0],256,symmetric=True,normed=True)  cont=greycoprops(glcm,'contrast') 
 diss=greycoprops(glcm,'dissimilarity') 
 homo=greycoprops(glcm,'homogeneity') 
 eng=greycoprops(glcm,'energy') 
 corr=greycoprops(glcm,'correlation') 
 ASM=greycoprops(glcm,'ASM') 
 featQF=[cont,diss,eng,corr,ASM,homo] 
 outt=np.array(featQF) 
 out=outt.reshape([1,6]) 
 y_pred1=svm.predict(out) 
 if y_pred1==1: 
 a="Tomato___Early_blight" 
 print('output is --------->>>>>>>>') 
 print('Tomato___Early_blight') 
 print('--------->>>>>')
 
 elif y_pred1==2: 
 a="Tomato___healthy" 
 print('output is --------->>>>>>>>') 
 print('Tomato___healthy') 
 print('--------->>>>>') 
 elif y_pred1==3: 
 a="Tomato___Late_blight" 
 print('output is --------->>>>>>>>') 
 print('Tomato___Late_blight') 
 print('--------->>>>>') 
 label1=Label(my_w,text="The Disease is predicted  
as",font=("Helvetica:",14)).grid(row=12,column=1) 
 label2=Label(my_w,text=a,font=("Helvetica:",14)).grid(row=13,column=1) submit=tk.Button(my_w,text="submit",command=Submit).grid(row=8,column=1) my_w.mainloop()

