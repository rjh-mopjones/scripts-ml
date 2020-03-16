import numpy as np
import math
data = [5.92, 2.28, 3.85, 5.17, 1.75]
components = [{"pi":0.5,"mu":3.34,"sigsq":1},{"pi":0.5,"mu":6.12,"sigsq":1}]

output=[]
output.append([])
print("Expectation")
print()
for x in data:
    for c in components:
        num = 0
        denom = 0
        strenom=""
        for a in components:
            curr = (a["pi"]/math.sqrt(2*math.pi*a["sigsq"]))*math.exp(-(((x-a["mu"])**2)/(2*a["sigsq"])))
            denom+= curr
            strenom+=(" "+str(curr)+" +")
        num+= (c["pi"]/math.sqrt(2*math.pi*c["sigsq"]))*math.exp(-(((x-c["mu"])**2)/(2*c["sigsq"])))
        print(str(num) + "/" + strenom[:-1])
        output[-1].append((num/denom))
    output.append([])    
print(output)

