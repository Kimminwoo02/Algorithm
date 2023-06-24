n= int(input())
data = list(map(int,input().split()))
data.sort()
target =int(input()) 
cnt = 0
lt = 0
rt = n-1

while lt <rt:
  tmp = data[lt] + data[rt] 
  if tmp  == target:
    cnt +=1
    lt +=1
  elif tmp > target: 
    rt-=1
  else:
    lt+=1
print(cnt)