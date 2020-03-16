import numpy as np
import math
data = [5.92, 2.28, 3.85, 5.17, 1.75]
components = [{"pi":0.5,"mu":3.34,"sigsq":1},{"pi":0.5,"mu":6.12,"sigsq":1}]

output=[]
for x in components:
    output.append([])
print(output)
    
print("Expectation")
print()
for x in data:
    i=0
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
        output[i].append((num/denom))
        i+=1
print(output)
sums = []
for each in output:
    total = 0
    for value in each:
        total+=value
    sums.append(total)

    
        
print()
print()
print()

print("Maximisation")
j=0
print()
print("k sums")
print(sums)

updated_means = []
print()
print("new means")
for c in components:
    means_workings = " mu_%d = (1/%.4f"%(j+1,sums[j])
    total = 0
    i=0
    while i < len(data):
        total+=(data[i]*output[j][i])
        means_workings+= " (%.4f * %.4f) +"%(data[i],output[j][i])
        i+=1
    means_workings=means_workings[:-1]+") = %.4f"%(total/sums[j])
    updated_means.append(total/sums[j])
    print(means_workings)
    j+=1
        
print(updated_means)

j=0
updated_vars = []
print()
print("new vars")
for c in components:
    vars_workings = " sigsq_%d = (1/%.4f"%(j+1,sums[j])
    total = 0
    i=0
    while i < len(data):
        total+=(output[j][i]*(data[i]-updated_means[j])**2)
        vars_workings+= " (%.4f *(%.4f -  %.4f) +"%(output[j][i],data[i],updated_means[j])
        i+=1
    vars_workings=vars_workings[:-1]+") = %.4f"%(total/sums[j])
    updated_vars.append(total/sums[j])
    print(vars_workings)
    j+=1


print(updated_vars)
i=0
print()
print("new mixing")
for each in sums:
    mixing = each/len(output[i])
    mixing_workings="pi_%d = (%.4f / %.4f) = %.4f"%(i+1,each, len(output[i]),mixing)
    i=i+1
    print(mixing_workings)



    
print()
print()
print()
print()
print("fitting")
components = [{"pi":0.61,"mu":2.65,"sigsq":0.85},{"pi":0.39,"mu":5.55,"sigsq":0.14}]
x=3.13

workings="p(x) = ("
total_workins =" = "
total=0
for c in components:
    workings+=" %.3f / sqrt(2pi%.3f)  *  e^( - %.3f - %.3f / 2 * %.3f) +"%(c["pi"],c["sigsq"],x,c["mu"],c["sigsq"])
    num= (c["pi"]/math.sqrt(2*math.pi*c["sigsq"]))
    denom= math.exp(-(x-c["mu"])**2/(2*c["sigsq"]))
    output = num*denom
    total+=output
    total_workins+=" %.5f +"%(output)
print(workings[:-1]+") = ")
print(total_workins[:-1]+"= %.5f"%(total))


    















    
    

