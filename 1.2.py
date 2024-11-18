def duplicates(input_string):
    lst_unique=[]
    lst_duplicates=[]
    for i in input_string:
        if i in lst_unique:
            lst_duplicates.append(i)
        else:
            lst_unique.append(i)

    print("unique characters are:",lst_unique)
    print("duplicates characters are:",lst_duplicates)

duplicates("Good Morning")



