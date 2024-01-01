Increasing brightness of the image using contrast enhancement as follows,  clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))  
 lab = cv2.cvtColor(k, cv2.COLOR_BGR2LAB) # convert from BGR to LAB color space  l, a, b = cv2.split(lab) # split on 3 different channels 
 l2 = clahe.apply(l) # apply CLAHE to the L-channel 
 lab = cv2.merge((l2,a,b)) # merge channels 
 img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR) # convert from LAB to BGR 
 image = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) 
 pixel_vals = image.reshape((-1,3)) 
 from skimage import color
 from skimage import io 
 pixel_vals = np.float32(pixel_vals) 
Then, applying K-means segmentation , 
 criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)  k = 2 
 retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 1,  
cv2.KMEANS_RANDOM_CENTERS) 
 centers = np.uint8(centers) 
 segmented_data = centers[labels.flatten()] 
 segmented_image = segmented_data.reshape((image.shape)) 
 aa=segmented_image 

