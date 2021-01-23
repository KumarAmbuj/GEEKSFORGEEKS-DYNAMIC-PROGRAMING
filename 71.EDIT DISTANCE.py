def findEditDistance(s1,s2):
    dp=[[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]

    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):

            if s1[i]==s2[j]:
                dp[i][j]=dp[i+1][j+1]+1
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j+1])

    lcs=dp[0][0]

    ans=len(s2)-lcs
    print(ans)

sr1 = "geek"
sr2 = "gesek"
findEditDistance(sr1,sr2)

sr1 = "sunday"
sr2 = "saturday"
findEditDistance(sr1,sr2)
