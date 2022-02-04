n,m = map(int,input().split())
dp = [[int(i) for i in input().split(" ")] for j in range(n)]
for i in range(1,m):
    dp[0][i] += dp[0][i-1]
for i in range(1,n):
    dp[i][0] += dp[i-1][0]
for i in range(1,n):
    for j in range(1,m):
        dp[i][j] += max(dp[i-1][j],dp[i][j-1])
print(dp[n-1][m-1])