n = int(input())
data1 = list(map(int,input().split()))

m = int(input())
data2 = list(map(int,input().split()))

dic = dict()
for i in data1:
  dic[i] = dic.get(i,0) + 1
for j in data2:
  if j in dic:
    print(dic[j], end=' ')
  else:
    print(0, end=' ')