N = int(input())

for n in range(N):
    K = int(input())
    if (K & 1):
        print("odd"); continue
    print("even")