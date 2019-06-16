A=input()
num=0
for i in range(len(A)):
  if(A[i].isdigit() or A[i].isalpha() or A[i]==' '):
    continue
  else:
    num=num+1
print(num) 
