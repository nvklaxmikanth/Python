def fun(a,s,l,n):
    if(s == n):
        print(*l)
    else:
        for i in range(len(a)):
            l[s] = a[i]
            fun(a,s+1,list(l),n)
l = list(input())
n = int(input()) #r value
fun(l,0,[0]*n,n)