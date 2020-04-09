n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = [A[i]+B[i] for i in range(n)]
print(*C)
