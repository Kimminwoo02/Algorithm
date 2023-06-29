n = int(input())
data = list(map(int,input().split()))
answer = 0

min_val = min(data)
max_val = max(data)

answer=min_val * max_val
print(answer)
