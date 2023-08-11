n = int(input())
wine = [0] * 10000
for i in range(n):
  wine[i] = int(input())

dy = [0] * 10000
dy[0] = wine[0]
dy[1] = wine[1] + wine[0]
dy[2] = max(wine[0]+wine[2],wine[2]+wine[1],dy[1])
for i in range(3,n):
  dy[i] = max(dy[i-1],dy[i-2]+wine[i],dy[i-3]+wine[i-1]+wine[i])

print(max(dy))