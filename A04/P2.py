import sys 

lst = {}
cn = {}

with open(sys.argv[1], 'r') as file:
    C = file.readline().split(",")
    total = int(file.readline()[:-1])
    coins = []
    t = total
    s = 0
    paths = []
    for i in C:
        coins.append(int(i))
        t -= (t // int(i)) * int(i)
        cn[i] = 0
    
    len = len(coins)
    coins.sort(reverse=True)

    lst["0"] = 0
    

    if(t == 0):
        t = total
        for i in range(1, total+1):
            lst[str(i)] = 10000000
            for j in coins:
                if (i - j >= 0):
                    lst[str(i)] = min(lst[str(i)], 1 + lst[str(i - j)])
            
        print(lst)
        print(lst[str(total)])
    else:
        print("There is no solution")

 
