a = list(map(int,input().split()))
n = len(a)
dp = [1]*n
for i in range(n):
    for j in range(i):
        if(a[i] > a[j] and dp[i] < dp[j] + 1):
            dp[i] = dp[j] + 1       
print(max(dp))