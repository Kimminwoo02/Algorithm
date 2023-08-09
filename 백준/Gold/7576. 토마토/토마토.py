from collections import deque

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]
dis= [[0] * n for _ in range(m)]
max_val = -2147000000

cnt = 0
flag = True

q = deque()
for i in range(m):
  for j in range(n):
    if board[i][j] == 1:
      q.append((i,j))
      
while q:
  now = q.popleft()
  for i in range(4):
    nx = now[0] + dx[i]
    ny = now[1] + dy[i]
    if 0<=nx<m and 0<=ny<n and board[nx][ny] == 0:
      board[nx][ny] = 1
      dis[nx][ny] = dis[now[0]][now[1]] + 1
      q.append((nx,ny))
    
for i in range(m):
  for j in range(n):
    if board[i][j] == 0:
      flag= False
    else:
      max_val = max(max_val,dis[i][j])
  
if flag == True:
  print(max_val)
else:
  print(-1)
               
               
      
  
    
