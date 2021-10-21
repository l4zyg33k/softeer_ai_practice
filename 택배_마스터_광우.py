import sys, itertools

def main():
    rail_cnt, wgt_max, wrk_cnt = list(map(int, input().split()))
    rails = list(map(int, input().split()[:rail_cnt]))
    wgt_sum = []

    for rail in itertools.permutations(rails, rail_cnt):
        c_idx, c_wrk, c_wgt, s_wgt = [0, 0, 0, 0]

        while c_wrk < wrk_cnt:
            if c_wgt + rail[c_idx] <= wgt_max:
                c_wgt += rail[c_idx]
                c_idx = (c_idx + 1) % rail_cnt
            else:
                s_wgt += c_wgt
                c_wgt = 0
                c_wrk += 1
            
        wgt_sum.append(s_wgt)

    print(min(wgt_sum))

if __name__ == "__main__":
    main()