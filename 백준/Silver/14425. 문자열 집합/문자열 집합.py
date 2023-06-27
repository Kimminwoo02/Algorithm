import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data1 =[]
data2 =[]

cnt=0
for _ in range(n):
  data1.append(input())

for _ in range(m):
  data2.append(input())


for i in data2:
  if i in data1:
    cnt+=1
print(cnt)
