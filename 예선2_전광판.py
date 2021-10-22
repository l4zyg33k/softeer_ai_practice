import sys

def solve():
    num = {
    ' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,1,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)
    }

    T = int(input())
    tests = []
    for t in range(T):
        tests.append(list(map(int, input().split()[:2])))

    for i in range(T):
        test = tests[i]
        A = "{0:>5d}".format(test[0])
        B = "{0:>5d}".format(test[1])
        tot_cnt = 0

        for j in reversed(range(5)):
            a = A[j]
            b = B[j]

            if a == b:
                continue

            a_arr = num.get(a)
            b_arr = num.get(b)
            cnt = 0

            for k in range(7):
                if a_arr[k] != b_arr[k]:
                    cnt += 1
            tot_cnt += cnt

        print(tot_cnt)

if __name__ == "__main__":
    solve()        