from collections import deque
n,m = map(int,input().split())
dis=[0] * 100001
ch= [0] * 100001
q = deque()
q.append(n)
res=0
while q:
    now = q.popleft()
    if now == m:
        break
    for next in (now+1,now-1,now*2):
        if 0 <= next <= 100000:
            if ch[next] == 0:
                q.append(next)
                ch[next] = 1
                dis[next] =dis[now] + 1

print(dis[m])

