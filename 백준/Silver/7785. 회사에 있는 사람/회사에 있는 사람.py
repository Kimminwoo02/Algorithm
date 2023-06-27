import sys
input = sys.stdin.readline

dic = dict()

n = int(input())
for _ in range(n):
  a, b = input().split()
  if b =='enter':
    dic[a] = b
  else:
    del(dic[a])

dic = sorted(dic.keys(),reverse=True)

for i in dic:
  print(i)
    

  
