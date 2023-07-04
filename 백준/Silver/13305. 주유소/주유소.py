n = int(input())
roads= list(map(int,input().split()))
prices= list(map(int,input().split()))
res = roads[0] * prices[0]
min_val = prices[0]

for i in range(1,n-1):
  if min_val > prices[i]:
    min_val = prices[i]  
  res += min_val * roads[i]
print(res)
  