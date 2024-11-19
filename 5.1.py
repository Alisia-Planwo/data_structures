lst1=[1,2,3,4,5,6,9,10]
lst2=[2,3,4,5,6,7,10]

for i in lst1:
    if i not in lst2:
        print("unique elements in lst1",i)

for j in lst2:
    if j not in lst1:
        print("unique elements in lst2",j)