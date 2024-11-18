from itertools import combinations
def subsets(input_tuple):
    sb=[]
    n=len(input_tuple)
    for i in range(n+1):
        sb.extend(combinations(input_tuple,i))
    print(sb)

inp=(1,2,3)
subsets(inp)