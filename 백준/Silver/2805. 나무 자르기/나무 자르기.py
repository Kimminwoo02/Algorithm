n,m = map(int,input().split())
data = list(map(int,input().split()))
lt,rt  = 0,max(data)
while lt<=rt:
  mid = (lt+rt)//2
  cnt = 0
  
  for i in data:
    if i >= mid:
      cnt += i-mid
  if cnt >= m:
    lt = mid+1
  else:
    rt = mid-1

print(rt)
