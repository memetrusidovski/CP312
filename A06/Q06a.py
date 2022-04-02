import sys

ans = []


def tsp(graph, v, currPos, n, count, cost):
    
    if (count == n and graph[currPos][0]):
        ans.append(cost + graph[currPos][0])
        return

    for i in range(n):
        if (v[i] == False and graph[currPos][i]):

            v[i] = True
            tsp(graph, v, i, n, count + 1,
                cost + graph[currPos][i])

            v[i] = False



with open(sys.argv[1], 'r') as file:
    V = int(file.readline()[:-1])
    Matrix = [[0 for x in range(V)] for y in range(V)]

    for line in file:
        C = line[:-1].split(" ")
        Matrix[int(C[0])][int(C[1])] = int(C[2])
        Matrix[int(C[1])][int(C[0])] = int(C[2])
    
    v = [False for i in range(V)]
    v[0] = True
    tsp(Matrix, v, 0, V, 1, 0)

    print(min(ans))


