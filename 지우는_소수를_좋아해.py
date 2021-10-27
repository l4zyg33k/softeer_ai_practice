import sys
import queue

def main():
    N, M = list(map(int, input().split()[:2]))

    global E
    E = [[-1 for i in range(N)] for j in range(N)]

    for i in range(M):        
        A, B, C = list(map(int, input().split()[:3]))

        if E[A - 1][B - 1] == -1 or E[A - 1][B - 1] > C:
            E[A - 1][B - 1] = C

        if E[B - 1][A - 1] == -1 or E[B - 1][A - 1] > C:
            E[B - 1][A - 1] = C

    global D
    D = {n:-1 for n in range(N)}

    dijkstra()

def dijkstra():
    D[0] = 0
    
    pq = queue.PriorityQueue()
    pq.put(0, 1)

    while pq.empty() == True:
        

def isPrime(n):
    flag = True

    if n == 1:
        pass
    elif n == 2:
        flag = False
    else:
        for i in range(2, n):
            if n % i == 0:
                flag = False
                break

    return flag

if __name__ == '__main__':
    main()