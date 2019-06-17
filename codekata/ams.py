A,B=map(int,input().split())
for x in range(A+1,B):
  sum =0
  temp =x
  while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
  if x==sum:
    print(x,end=' ')
