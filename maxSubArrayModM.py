def find(a,n,m):
    for i in range(n,m):
        if(a[i]):
            return i
    return -1
n,m = map(int,input().split())
a = list(map(int,input().split()))
p = [0]*n 
t = [0]*m
p[0] = a[0]
t[a[0]] = 1
l = []
for i in range(1,n):
    p[i] = (a[i]+p[i-1]+m)%m 
    v = find(t,p[i],m)
    if(v != -1):
        l.append((p[i]-v+m)%m)
    t[p[i]] = 1
    l.append(p[i])
print(max(l))