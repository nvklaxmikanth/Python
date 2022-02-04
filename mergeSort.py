def merge(a,l,m,h):
    n1 = m-l+1 
    n2 = h-m
    x = []
    y = []
    for i in range(n1):
        x.append(a[l+i])
    for j in range(n2):
        y.append(a[m+1+j])
    i = j = 0 
    k = l 
    while(i < n1 and j < n2):
        if(x[i] <= y[j]):
            a[k] = x[i]
            i += 1 
        else: 
            a[k] = y[j]
            j += 1 
        k += 1
    while(i < n1):
        a[k] = x[i]
        i += 1 
        k += 1 
    while(j < n2):
        a[k] = y[j]
        j += 1 
        k += 1         
def mergesort(a,l,h):
    if(l < h):
        mid = l + (h-l)//2 
        mergesort(a,l,mid)
        mergesort(a,mid+1,h)
        merge(a,l,mid,h)
a = list(map(int,input().split()))
mergesort(a,0,len(a)-1)
print(a)