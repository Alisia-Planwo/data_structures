def inverted_dic(dic):
    rev={value:key for key,value in dic.items()}
    return rev

dic={'a':1,'b':2,'c':3}
inv=inverted_dic(dic)

print("The original dictionary:",dic)
print("The inverted dictionary:",inv)