t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    if k>min(a):
        print(k-min(a))
    else:
        print(0)
