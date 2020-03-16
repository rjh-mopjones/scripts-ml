clusters = [[0.06, 0.37],[1.75, 1.35]]
data = [[1.23, 0.11],[0.83, -0.59],[0.23, 2.06],[1.51, 1.35],[-1.09,0.53],[-0.5,1.01],[-0.08,0.25],[1.49,1.83],[-0.2,-0.77],[2.26,0.88]]
import math

assignment = []
for each in data:
    assignment.append(0)

i=0
min_distance = 10000000000000000000000
while i < len(data):
    j =0
    while j <len(clusters):
        cluster_distance= math.sqrt((data[i][0] - clusters[j][0])**2 + (data[i][1] - clusters[j][1])**2 )
        print()
        print("data point %d cluster %d distance:- sqrt((%.2f - %.2f)^2 + (%.2f - %.2f)^2 = %.4f )"
        %(i+1, j+1, data[i][0], clusters[j][0], data[i][1], clusters[j][1], cluster_distance))
        if cluster_distance < min_distance:
            assignment[i]=(j+1)
            min_distance = cluster_distance
        j+=1
    min_distance = 10000000000000000000000
    i+=1

print()
print("assignments:-")
print(assignment)
print()

i=0
while i < len(clusters):
    x=[]
    y=[]
    new_cluster_string_x = "new cluster %d x coord:- " % (i+1)
    new_cluster_string_y = "new cluster %d y coord:- " % (i+1)
    j =0
    while j < len(data):
        if assignment[j] == (i+1):
            x.append(data[j][0])
            y.append(data[j][1])
            new_cluster_string_x += " %.2f +" %(data[j][0])
            new_cluster_string_y += " %.2f +" %(data[j][1])
        j+=1
    
    new_cluster_string_x = new_cluster_string_x[:-1]
    new_cluster_string_y = new_cluster_string_y[:-1]
    new_x = sum(x)/len(x)
    new_y = sum(y)/len(y)
    new_cluster_string_x += "  = %.4f"%(new_x)
    new_cluster_string_y += "  = %.4f"%(new_y)
    print(new_cluster_string_x)
    print(new_cluster_string_y)
    print("new cluster %d = %.4f , %.4f" %(i+1, new_x, new_y))
    i+=1
            
        

    

