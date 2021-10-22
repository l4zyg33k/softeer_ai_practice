import sys

def solve():
    M, N, K = list(map(int, input().split()[:3]))
    M_menu = list(map(int, input().split()[:M]))
    N_menu = list(map(int, input().split()[:N]))
    isSecret = False

    for i in range(N):
        match_cnt = 0
        for j in range(M):
            k = (i + j) % N
            if M_menu[j] == N_menu[k]:
                match_cnt += 1
            else:
                break
        if match_cnt == M:
            isSecret = True
    print("secret " if isSecret == True else "normal")

if __name__ == "__main__":
    solve()        