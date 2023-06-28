n = int(input())
data = list(map(int,input().split()))
res = sorted(set(data))

dic = {res[i]:i for i in range(len(res))}

for i in data:
  print(dic[i],end=' ')
