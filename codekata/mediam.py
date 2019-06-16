A=int(input())
B=list(map(int,input().split()))
B.sort()
mid=B[int(A/2)]
print(mid)
