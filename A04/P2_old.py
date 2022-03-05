import sys 


with open(sys.argv[1], 'r') as file:
    C = file.readline().split(",")
    total = int(file.readline())
    coins = []
    t = total

    for i in C:
        coins.append(int(i))
        t -= (t // int(i)) * int(i)
        

    coins.sort(reverse=True)

    if(t == 0):
        for i in coins:
            if(total > 0):
                print(str(total // i) + " packages of size " + str(i))
                total -= (total // i) * i
        
    else:
        print("There is no solution")
