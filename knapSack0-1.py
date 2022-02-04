p = list(map(int,input().split()))
w = list(map(int,input().split()))
n = len(p)
c = int(input())
dp = [[0]*(c+1) for i in range(n+1)]
for i in range(n+1):
    for j in range(c+1):
        if(w[i-1] <= j):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i-1]] + p[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][c])