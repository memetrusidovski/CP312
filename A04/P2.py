import sys 

lst = {}
cn = {}

with open(sys.argv[1], 'r') as file:
    C = file.readline().split(",")
    total = int(file.readline())
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
        for i in range(1, total+1):
            lst[str(i)] = 10000000
            t = total
            if(i < total):
                for j in coins:
                    if (i - j >= 0):
                        lst[str(i)] = min(lst[str(i)], 1 + lst[str(i - j)])
            else:
                for j in coins:
                    if (i - j >= 0):
                        lst[str(i)] = min(lst[str(i)], 1 + lst[str(i - j)])
                        
        print(lst[str(total)])


    else:
        print("-1")
        print("There is no solution")

 
