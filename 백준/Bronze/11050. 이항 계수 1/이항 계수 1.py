import sys
input = sys.stdin.readline

n,m = map(int,input().split())

result = 1 
for i in range(m):
  result *= n
  n -= 1

res  = 1 
for i in range(2,m+1):
  res *= i

print(result // res)