n = int(input())
data = [0] * 301

for i in range(n):
  data[i] = int(input())

dy = [0] * 301
dy[0] = data[0]
dy[1] = data[0] +data[1]
dy[2] = max(data[0]+data[2],data[1]+data[2])

for i in range(3,n):
  dy[i] = max(dy[i-3]+data[i-1]+data[i],dy[i-2]+data[i])
print(dy[n-1])