def DFS(graph,g,ch):
  ch[g] = 1
  for i in graph[g]:
    if ch[i]==0:
      DFS(graph,i,ch)

n,m = map(int,input().split())
graph =[[] for _ in range(n+1)]
ch = [0]*(n+1)
cnt=0

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
for i in range(1,n+1):
  if ch[i]==0:
    DFS(graph,i,ch)
    cnt+=1
print(cnt)