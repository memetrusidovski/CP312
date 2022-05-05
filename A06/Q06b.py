import sys
import time
start = time.time()

ans = []
minSoFar = 1000000000



def tsp(graph, v, currentPosition, n, count, cost):
    global minSoFar
    if (count == n and graph[currentPosition][0]):
        minSoFar = cost + graph[currentPosition][0]
        ans.append(cost + graph[currentPosition][0])
        return

    for i in range(n):
        if (v[i] == False and graph[currentPosition][i]):

            v[i] = True
            
            if(int(cost + graph[currentPosition][i]) < minSoFar):

                tsp(graph, v, i, n, count + 1,
                    cost + graph[currentPosition][i])

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


end = time.time()
print(end - start)
