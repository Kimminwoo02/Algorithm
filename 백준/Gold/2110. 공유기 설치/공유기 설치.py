def count(mid):
  ep = data[0]
  cnt = 1
  for i in range(1,n):
    if data[i]-ep >= mid:
      cnt +=1
      ep = data[i]
  return cnt

n,m = map(int,input().split())
data = []
for _ in range(n):
  data.append(int(input()))
data.sort()
lt=0
rt = max(data)
while lt<=rt:
  mid = (lt + rt) //2
  if count(mid) >= m:
    lt = mid +1
  else:
    rt = mid -1
print(rt)