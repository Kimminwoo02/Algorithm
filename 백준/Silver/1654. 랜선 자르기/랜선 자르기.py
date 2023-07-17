def count(mid):
  cnt = 0
  for i in data:
    cnt += i//mid
  return cnt

n,m = map(int,input().split())
data = []
for _ in range(n):
  data.append(int(input()))
lt =1
rt = max(data)
res=0
while lt<=rt:
  mid = (lt+rt)//2

  if count(mid) >= m:
    res = mid
    lt = mid +1
  else:
    rt = mid-1
print(res)
