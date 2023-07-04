n = int(input())
data = list(map(int,input().split()))
data.sort()
total = 0
sum=0
for i in data:
  sum +=i
  total+=sum
print(total)