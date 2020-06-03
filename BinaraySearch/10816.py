import sys
N = int(sys.stdin.readline())
N_list = list(map(int, input().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, input().split()))

for i in M_list:
    cnt = 0
    for j in N_list:
        if i == j:
            cnt += 1
    print(cnt, end=" ")
