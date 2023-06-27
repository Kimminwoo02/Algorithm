import sys
input = sys.stdin.readline

dic = dict()
n,m = map(int,input().split())
cnt =0
for _ in range(n):
  key = input()
  dic[key] = 1

for _ in range(m):
  t = input()
  if t in dic:
    cnt+=1
print(cnt)