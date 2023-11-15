import sys
input = sys.stdin.readline

tc = 1
while True:
  a,b,c = map(int,input().split())
  num = 0
  n = 0
  m = 0
  if a==0 and b==0 and c==0:
    sys.exit(0)
  else:
    n = c // b
    m = c % b
    if m > a:
      m = a
    print("Case %d: %d" %(tc,(n*a) + m))
    tc +=1