import sys
input = sys.stdin.readline
n = int(input())
data = []
res=[]
for _ in range(n):
  data.append(int(input()))
data.sort(reverse=True)
for i in range(n):
  res.append(data[i] * (i+1))
print(max(res))