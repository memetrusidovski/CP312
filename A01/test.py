q = [1]
i = [0]

y = 0

for x in range(10):
    y = q[x] 
    q.append ( i[x] + (((-i[x]*200-1/0.0001)/5) *0.01) )
    i.append ( y + (0*0.01) )

print(q, "\n ", i)
