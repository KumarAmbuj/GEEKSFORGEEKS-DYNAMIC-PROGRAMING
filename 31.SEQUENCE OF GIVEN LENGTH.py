def findsequence(m,n,dp):
    if n==1:
        dp[n][m]=m
        return m
    if dp[n][m]!=0:
        return dp[n][m]

    res=0
    if m>(2**(n-1)):
        res=findsequence(m-1,n,dp)+findsequence(m//2,n-1,dp)
    elif m==(2**(n-1)):
        res=findsequence(m//2,n-1,dp)
    dp[n][m]=res
    return res


def findgivensequence(m,n):
    dp=[[0 for j in range(m+1)] for i in range(n+1)]

    res=findsequence(m,n,dp)
    print(res)

findgivensequence(10,4)
findgivensequence(5,2)