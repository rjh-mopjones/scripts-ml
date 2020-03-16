data = [7.42, 2.28, 3.45, 7.17, 1.75]
x = 3.13
h=1
import math

array = []

workings = "p(x) = 1/%d * ("%(len(data))
workings2 = "p(x) = 1/%d * ("%(len(data))

for each in data:
    ans = (1/math.sqrt(2*math.pi*h**2))*math.exp(-(((each-x)**2)/(2*h**2)))
    array.append(ans)
    workings += ("  1/sqt(2pi%d^2) e^(-(%.3f - %.3f)/2%d^2)  +"%(h,each,x,h))
    workings2+=" %.4f +" % (ans)
    
workings = workings[:-1] + ")"
workings2 = workings2[:-1] + ")"
print(workings)
print(workings2)
final = sum(array)/len(array)
print("p(x) = %.4f"%(final))


