a = [1, 5, 8, 9, 10, 17, 17, 20 ];
n = len(a)
dp = [0]*(n+1)
dp[0] = 0
INT_MIN = -32767
for i in range(1,n+1):
    v = INT_MIN
    for j in range(i):
        v = max(v,a[j]+dp[i-j-1])
    dp[i] = v
print(dp[n])