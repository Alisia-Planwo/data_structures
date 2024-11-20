def mov_avg(numbers,window_size):

    em=[]
    for i in numbers:
        em.append(i)
        if len(em)>window_size:
            em.pop(0)
        yield sum(em)/len(em)

data=[10,20,30,40,50]
for avg in mov_avg(data,3):
    print(avg)