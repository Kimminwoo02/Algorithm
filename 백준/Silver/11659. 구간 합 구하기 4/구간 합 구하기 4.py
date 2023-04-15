import sys
input = sys.stdin.readline

a,b = map(int,input().split())
data =list(map(int,input().split()))
total= 0
pre = [0]
for i in data:
  total += i 
  pre.append(total)
for _ in range(b):
  n,m = map(int,input().split())
  print(pre[m] - pre[n-1])
  
  