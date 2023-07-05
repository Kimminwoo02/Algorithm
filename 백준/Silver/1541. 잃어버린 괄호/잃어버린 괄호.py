n = input().split('-')
num = []

for i in n:
  sum = 0
  tmp = i.split('+')
  for j in tmp:
    sum += int(j)
  num.append(sum)

res=num[0]
for i in range(1,len(num)):
  res -= num[i]
print(res)