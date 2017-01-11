import numpy as np 

x=[15,12,8,8,7,7,7,6,5,3]
y=[10,25,17,11,13,17,20,13,9,15]

print round(np.corrcoef(x,y)[0,1],3)