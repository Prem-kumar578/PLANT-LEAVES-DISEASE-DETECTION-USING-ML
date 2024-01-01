for file in glob.glob(path): 
 orig=cv2.imread(file) 
 print(file) 
 gray=cv2.cvtColor(orig,cv2.COLOR_RGB2GRAY) 
 plt.imshow(cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)) 
 img=gray 
 thresh = cv2.threshold(img,np.mean(img) , 255, cv2.THRESH_BINARY_INV)[-1]   img=thresh
 
 edges =cv2.dilate(cv2.Canny(img, 0, 255), None)  
 img=cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB) 
 cnt=sorted(cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-  2], key=cv2.contourArea)[-1] 
 mask = np.zeros((256,256), np.uint8) 
 masked=(cv2.drawContours(mask, [cnt],-1, 255, -1)) 
 dst= cv2.bitwise_and(orig, orig, mask=mask) 
 segmented=(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)) 
 k=cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB) 

