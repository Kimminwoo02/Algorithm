import sys
sys.setrecursionlimit(10 ** 6)

def DFS(x, y, h):
    global n
    ch[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and ch[nx][ny]==0 and board[nx][ny] > h:
            DFS(nx, ny, h)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
cnt = 0
res = 0
for h in range(100):
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > h and ch[i][j] == 0:
                cnt += 1
                DFS(i, j, h)

    res = max(cnt, res)
print(res)