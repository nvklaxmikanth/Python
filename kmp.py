s = input()
p = input()
n = len(s)
m = len(p)
f = [0]*m
j = 0
i = 1
while(i<m):
    if(p[i] == p[j]):
        f[i] = j+1
        i+=1 
        j+=1
    elif(j>0):
        j = f[j-1] 
    else:
        i += 1
j = 0
i = 1
while(i<n):
    if(s[i] == p[j]):
        if(j == m-1):
            print(i-j,i)
            break
        else:
            i+=1 
            j+=1
    elif(j>0):
        j = f[j-1]
    else:
        i+=1