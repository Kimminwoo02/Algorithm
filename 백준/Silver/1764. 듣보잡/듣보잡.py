# import sys
# input = sys.stdin.readline

n,m = map(int,input().split())
dic = dict()
for _ in range(n):
  a = input()
  dic[a] = 1
  
for _ in range(m):
  b = input()
  dic[b] = dic.get(b,0) + 1

dic = sorted(dic.items())
cnt =0
res =[]
for i in dic:
  if i[1]==2:
    cnt+=1
    res.append(i[0])

print(cnt)
for i in res:
  print(i)

  