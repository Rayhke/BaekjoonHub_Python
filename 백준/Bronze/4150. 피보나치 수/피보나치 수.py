N = int(input())
Arr = []

Arr.append(1)
Arr.append(1)

for n in range(2, N, 1):
    Arr.append(Arr[n - 1] + Arr[n - 2])
    
print(Arr[N - 1])