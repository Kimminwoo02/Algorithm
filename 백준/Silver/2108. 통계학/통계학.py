import sys

n=int(input())
data=[]
for _ in range(n):
  data.append(int(sys.stdin.readline().rstrip())) 
data.sort()  
lt=0
rt=len(data)-1
mid = (lt+rt) // 2
  
print(round((sum(data) / len(data))))
print(data[mid])

dic = dict()
tmp = []

for i in data:
  dic[i] = dic.get(i,0) + 1
max_val = max(dic.values())
for k,v in dic.items():
  if v ==max_val:
    tmp.append(k)

if len(tmp) > 1:
  print(tmp[1])
else:
  print(max(dic,key=dic.get))


print(max(data)-min(data))

