class Solution:
    def rob(self, a: List[int]) -> int:
        dp = [0]*len(a)
        dp[0] = a[0]
        if(len(a) >= 2):
            dp[1] = max(a[0],a[1])
        for i in range(2,len(a)):
            dp[i] = max(a[i]+dp[i-2],dp[i-1])
        return dp[len(a)-1]