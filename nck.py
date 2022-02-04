def nck(n,k):
    if(table[n][k] != -1):
        return table[n][k]
    if(k == 0 or k == n):
        return 1
    else:
        table[n][k] = nck(n-1,k-1) + nck(n-1,k)
        return table[n][k]
v = 100
table = [[-1]*(v) for i in range(v)]
n,k = map(int,input().split())
print(nck(n,k))