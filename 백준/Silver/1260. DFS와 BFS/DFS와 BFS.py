from collections import deque
def DFS(v):
  global a,ch
  ch[v] = 1
  print(v,end=' ')
  for i in range(1,a+1):
    if ch[i]==0 and graph[v][i]==1:
      DFS(i)
      
def BFS(v):
  global a,ch
  ch[v] = 1
  q = deque()
  q.append(v)
  while q:
    now = q.popleft()
    print(now,end=' ')
    for i in range(1,a+1):
      if ch[i] == 0 and graph[now][i]:
        q.append(i)
        ch[i] =1


a,b,c =map(int,input().split())
graph=[[0] * (a+1) for _ in range(a+1)]
ch=[0] * (a+1)

for _ in range(b):
  n,m =map(int,input().split())
  graph[n][m]=1
  graph[m][n]=1

DFS(c)

print()
for i in range(len(ch)):
  ch[i] = 0
BFS(c)