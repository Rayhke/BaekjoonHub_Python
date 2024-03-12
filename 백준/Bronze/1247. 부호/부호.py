import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    M = 0

    for _ in range(N):
        M += int(input())

    if M > 0:
        print("+")
    elif M < 0:
        print("-")
    else:
        print(0)