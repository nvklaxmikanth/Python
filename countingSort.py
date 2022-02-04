a = list(map(int,input().split()))
maxv = 10
n = len(a)
l = [0]*maxv
s = [0]*n
for i in a:
    l[i] += 1
for i in range(1,maxv):
    l[i] = l[i] + l[i-1]
for i in a:
    s[l[i]-1] = i 
    l[i] -= 1 
print(s)