n,m = map(int,input().split())
data = []
for _ in range(n):
  data.append(int(input()))
data.sort(reverse=True)
cnt = 0
for i in data:
  if m == 0:
    break
  if i > m:
    continue
    
  else:
    while m>=i:
      cnt +=1
      m -= i
print(cnt)