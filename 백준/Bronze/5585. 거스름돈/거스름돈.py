import sys
input = sys.stdin.readline

n = int(input())
n = 1000-n
res = 0
coins = [500,100,50,10,5,1]
for coin in coins:
  res += n // coin
  n = n%coin
print(res)

