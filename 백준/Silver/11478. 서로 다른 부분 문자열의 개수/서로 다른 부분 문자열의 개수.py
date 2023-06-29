n = input()
res = set()

for i in range(len(n)):
  for j in range(i,len(n)):
    tmp = n[i:j+1]
    res.add(tmp)
print(len(res))