import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  a = int(input())
  data = []
  for _ in range(a):
    x,y = map(int,input().split())
    data.append((x,y))
  data.sort()
  
  cnt = 1
  idx = data[0][1]
  for i in range(1,a):
    if idx > data[i][1]:
      cnt += 1
      idx = data[i][1]
  print(cnt)