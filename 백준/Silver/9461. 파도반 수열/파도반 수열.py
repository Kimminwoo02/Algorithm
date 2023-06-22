import sys
input = sys.stdin.readline

n = int(input())
d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2
for i in range(6,101):
  d[i] = d[i-1] + d[i-5]
for _ in range(n):
  a = int(input())
  print(d[a])
  
  
  
  