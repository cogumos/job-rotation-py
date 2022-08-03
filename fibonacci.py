n = int(input())
before = 0
after = 1
sum = 0

while(before < n):
  sum = before + after
  before = after
  after = sum

if(n==before):
  print("Faz parte")
  
else:
  print("Nao faz parte")
