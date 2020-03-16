import math
import numpy as np
data = np.array([[1.23, 0.11],[0.83, -0.59],[0.23, 2.06],[1.51, 1.35],[-1.09,0.53],[-0.5,1.01],[-0.08,0.25],[1.49,1.83],[-0.2,-0.77],[2.26,0.88]])
x = np.array([[3.13,3.13]]).T
d = len(x)

data_mean = np.mean(data,axis=0).T
print("u = 1/%d * "%(len(data)) + np.array2string(data_mean))
print()
mean = np.array([np.mean(data, axis=0)]).T

covar=0
workins = "E = 1/%d *"%(len(data))
for each in data:
   workins+=" ("+np.array2string(each)+" - "+np.array2string(mean)+")"+"("+np.array2string(each)+" - "+np.array2string(mean)+")^T +\n"
    
   covar+=(each - mean)*(each-mean).T
print(workins[:-2])
covar = covar/len(data)
print("=" + np.array2string(covar))
print()


x_m = x - mean
print("x = "+  np.array2string(x))
print("u = "+ np.array2string(mean))
print("E = "+ np.array2string(covar))
print()
print("p(X) = ")
print(1. / (np.sqrt((2 * np.pi)**d * np.linalg.det(covar))) * 
 np.exp(-(np.linalg.solve(covar, x_m).T.dot(x_m)) / 2))
