import math

def distance(a,b):
    ds=math.sqrt((a[0]-b[0])**2 +
                 (a[1]-b[1])**2 +
                 (a[2]-b[2])**2)
    return ds

a=(1,2,3)
b=(2,3,4)
print("The euclidean distance is",distance(a,b))