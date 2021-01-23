def findlongestcommonsubstring(s1,s2):
    dp=[[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    mx=0
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):


            c1=s1[i-1]
            c2=s2[j-1]

            if c1==c2:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=0

            if dp[i][j]>mx:
                mx=dp[i][j]
    print(mx)

s1 = 'GeeksforGeeks'
s2 = 'GeeksQuiz'

findlongestcommonsubstring(s1,s2)

s1 = 'abcdxyz'
s2 = 'xyzabcd'

findlongestcommonsubstring(s1,s2)
