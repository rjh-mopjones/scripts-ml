data = [7.42, 2.28, 3.45, 7.17, 1.75]
x = 3.13
import math
mean = sum(data)/len(data)
sigma_sq = 0
workings_sigma1 = "sigma_squared = 1/%d * ("%(len(data))
workings_sigma2 = "sigma_squared = 1/%d * ("%(len(data))
for each in data:
    sigma_sq += (each - mean)**2
    workings_sigma1+= "  (%.4f - %.4f)^2 +" %(each, mean)
    workings_sigma2+= "  %.4f +" %(sigma_sq)  
sigma_sq = sigma_sq/len(data)
workings_sigma1 = workings_sigma1[:-1] + ")"
workings_sigma2 = workings_sigma2[:-1] + ")"
print(workings_sigma1)
print(workings_sigma2)
print("= %.4f"%(sigma_sq))

    
print("N = 1/sqt(2pi%.4f) e^(-(%.3f - %.3f)/2%.4f^2)"%(sigma_sq,x,mean,sigma_sq))
ans = (1/math.sqrt(2*math.pi*sigma_sq))*math.exp(-(((x-mean)**2)/(2*sigma_sq)))
print("= %.4f"%(ans))
