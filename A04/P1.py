import sys 

C = []
sum = 0

with open(sys.argv[1], 'r') as file:
    C = file.readline()[:-1].split(",")
    plus = int(file.readline()[:-1])
    minus = int(file.readline())

    sort = []
    for i in C:
        sort.append(int(i))
        

    sort.sort(reverse=True)
    sum += sort.pop(0)

    for i in sort:
        if (plus > 0):
            sum += i
            plus -= 1
        else:
            sum -= i

print(sum)