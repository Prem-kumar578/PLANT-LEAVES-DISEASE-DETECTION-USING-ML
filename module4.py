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
avgarray=np.array([]) 
feat=[] 
z=aa[:,:,0]; 
#print(str(len(aa))) 
glcm=greycomatrix(z,[5],[0],256,symmetric=True,normed=True) 
cont=greycoprops(glcm,'contrast') 
diss=greycoprops(glcm,'dissimilarity') 
homo=greycoprops(glcm,'homogeneity') 
eng=greycoprops(glcm,'energy') 
corr=greycoprops(glcm,'correlation') 
ASM=greycoprops(glcm,'ASM') 
feat=[cont,diss,eng,corr,ASM,homo] 
avgarray=np.append(avgarray,feat) 

