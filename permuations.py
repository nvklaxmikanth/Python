def fun(a,s,n):
    if(s == n):
        print(*a)
    else:
        for i in range(s,n):
            a[s],a[i] = a[i],a[s]
            fun(list(a),s+1,n)
            a[s],a[i] = a[i],a[s]
l = list(input())
fun(l,0,len(l))