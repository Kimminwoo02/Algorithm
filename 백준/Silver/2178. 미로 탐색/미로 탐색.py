from collections import deque

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n,m =map(int,input().split())
board =[]
for i in range(n):
  board.append(list(map(int,input())))
cnt=[[0] * m for _ in range(n)]

q = deque()
q.append((0,0))

while q:
  now = q.popleft()
  for i in range(4):
    nx = now[0] + dx[i]
    ny = now[1] + dy[i]
    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 :
      board[nx][ny] = 0
      cnt[nx][ny] = cnt[now[0]][now[1]]+1
      q.append((nx,ny))


print(cnt[n-1][m-1]+1)
