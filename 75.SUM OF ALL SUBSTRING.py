def findsumofallsubstring(s):
    dp=[0 for i in range(len(s))]

    for i in range(len(s)):
        dp[i]=(i+1)*int(s[i])+10*(dp[i-1] if i>=1 else 0)
    sum=0
    for i in range(len(s)):
        sum+=dp[i]

    print(sum)
findsumofallsubstring('1234')

findsumofallsubstring('421')