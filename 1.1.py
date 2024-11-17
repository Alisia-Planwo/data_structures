import timeit

n=10**6

lst=list(range(n))
tpl=tuple(range(n))
st=set(range(n))

lst_time=timeit.timeit(stmt="10 in lst",globals=globals(),number=1)
tpl_time=timeit.timeit(stmt="10 in tpl",globals=globals(),number=1)
st_time=timeit.timeit(stmt="10 in st",globals=globals(),number=1)

print("time taken in list:",lst_time)
print("time taken in tuple:",tpl_time)
print("time taken in set:",st_time)