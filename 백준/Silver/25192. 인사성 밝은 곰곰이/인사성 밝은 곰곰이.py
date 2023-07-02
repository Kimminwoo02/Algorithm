n=int(input())
dic={}
cnt=0

for _ in range(n):
    data=input()

    if data=='ENTER':
        for key,value in dic.items():
            if value==1:
                cnt+=1
        dic={}
    else:
        if data not in dic:
            dic[data]=1

for key,value in dic.items():
    if value==1:
        cnt+=1

print(cnt)