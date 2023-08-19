n,m = map(int,input().split())
data =[]
res=[]
for _ in range(n):
    data.append(input())
for i in range(n-7):
    for j in range(m-7):
        val1 = 0
        val2 = 0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y) % 2 ==0:
                    if data[x][y]=='W':
                        val1 +=1
                    elif data[x][y]=='B':
                        val2 +=1
                else:
                    if data[x][y] =='B':
                        val1+=1
                    else:
                        data[x][y] =='W'
                        val2+=1
        res.append(val1)
        res.append(val2)
print(min(res))