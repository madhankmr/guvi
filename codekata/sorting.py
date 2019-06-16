A=int(input())
B=list(map(int,input().split()))
if (A==len(B)):
  B.sort()
  for i in B:  
    print(i,end=" ")
