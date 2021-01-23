def findlcs(s1,s2,s3):
    dp=[[[0 for k in range(len(s3)+1)] for j in range(len(s2)+1)] for i in range(len(s1)+1)]

    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            for k in range(len(s3)-1,-1,-1):


                if s1[i]==s2[j] and s1[i]==s3[k]:
                    dp[i][j][k]=1+dp[i+1][j+1][k+1]

                else:
                    dp[i][j][k]=max(dp[i+1][j][k],dp[i][j+1][k],dp[i][j][k+1])
    print(dp[0][0][0])


s1 = "geeks"
s2 = "geeksfor"
s3 = "geeksforgeeks"

findlcs(s1,s2,s3)

s1 = "abcd1e2"
s2 = "bc12ea"
s3 = "bd1ea"
findlcs(s1,s2,s3)