def dfs(L):
  global cnt
  if L==n:
    cnt+=1
    return
  for j in range(n):
    if ch1[j] == ch2[L+j] == ch3[L-j] == 0:
      ch1[j] = ch2[L+j] =ch3[L-j] = 1
      dfs(L+1)
      ch1[j] = ch2[L+j] =ch3[L-j] = 0

n = int(input())
cnt = 0
ch1 = [0] * n
ch2 = [0] * (2*n)
ch3 = [0] * (2*n)
dfs(0)
print(cnt)