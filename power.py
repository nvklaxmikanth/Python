def fun(n,k):
    if(k == 0):
        return 1 
    t = fun(n,int(k/2))
    if(k%2):
        return n*t*t 
    return t*t
n,k = map(int,input().split())
print(fun(n,k))