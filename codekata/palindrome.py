A=int(input())
temp=A
reverse=0
while(A>0):
 dig=A%10
 reverse=reverse*10+dig
 A=A//10
if(temp==reverse):
 print("yes")
else:
  print("no")
 
