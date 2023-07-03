n = int(input())
flag = 0
data = set()
for _ in range(n):
  a,b =input().split()
  if a=='ChongChong' or b =='ChongChong':
    data.add(a)
    data.add(b)
  if a in data or b in data:
    data.add(a)
    data.add(b)
print(len(data))