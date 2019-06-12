M=['a','e','i','o','u']
S=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
C=input()
if C in S:
 if C in M:
  print("Vowel")
 else:
  print("Constant")
else:
 print("invalid")
