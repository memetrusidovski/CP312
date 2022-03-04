import timeit

start = timeit.default_timer()

n = 100
sum = 0

#Your statements here
for i in range(n):
    for j in range(i*i):
        if (j % i == 0):
            for k in range(j):
                sum += 1

stop = timeit.default_timer()

print('Time: ', stop - start)
