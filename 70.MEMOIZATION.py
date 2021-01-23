def minstep(n,dp):
    if n==1:
        return 0
    if dp[n]!=0:
        return dp[n]

    mn=0
    mn=minstep(n-1,dp)

    if n%2==0:
        mn=min(mn,minstep(n//2,dp))
    if n%3==0:
        mn=min(mn,minstep(n//3,dp))

    dp[n]=mn+1
    return dp[n]


def findminstep(n):
    dp=[0 for i in range(n+1)]
    dp[1]=0

    ans=minstep(n,dp)

    print(ans)

findminstep(10)