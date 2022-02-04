n = int(input())
a = list(map(int,input().split()))
dp = [0]*n
if(a[0] > 0):
    dp[0] = a[0]
for i in range(1,n):
    if(dp[i-1]+a[i] > 0):
        dp[i] = dp[i-1]+a[i]
print(max(dp))