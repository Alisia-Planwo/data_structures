def find_subsets(input_set):
    if not input_set:
        return [[]]

    small_set=find_subsets(input_set[1:])
    curr_element=input_set[0]

    org=[subsets+[curr_element]for subsets in small_set]

    return org + small_set

input_set=[1,2,3]
print(find_subsets(input_set))



