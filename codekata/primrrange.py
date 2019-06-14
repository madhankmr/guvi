A,B=map(int,input().split())
for m in range(A+1,B):
 if m>1:
  for i in range(2,m):
   if(m%i==0):
    break
  else:
   print(m,end=" ")
