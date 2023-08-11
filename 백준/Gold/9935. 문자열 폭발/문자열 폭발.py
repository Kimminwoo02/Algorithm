data = input()
ans = input()
n = len(ans) 
stack = []

for i in data:
  stack.append(i)
  if stack[-n:len(stack)] == [*ans]:
    for _ in range(n):
      stack.pop()
      
if len(stack) == 0:
  print("FRULA")
else:
  stack = "".join(map(str,stack))
  print(stack)
  
  