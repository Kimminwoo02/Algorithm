e,s,m = map(int,input().split())
e1 = 1
s1 = 1
m1 = 1
cnt = 1
while True:
  if e1 == e and s1 == s and m1 == m:
    print(cnt)
    break
  cnt += 1
  e1 = (e1%15) + 1
  s1 = (s1%28) + 1
  m1 = (m1 % 19) + 1
  