def rotate(mx):
    n=len(mx)
    for i in range(n):
        for j in range(i+1,n):
            mx[i][j],mx[j][i]=mx[j][i],mx[i][j]

    for i in mx:
        i.reverse()

    return mx

matrix=[1,2,3],[4,5,6],[7,8,9]
print(rotate(matrix))




