def findsequence(n,diff,dp):
    if abs(diff)>n:
        return 0
    if n==1 and diff==0:
        return 2
    if n==1 and abs(diff)==1:
        return 1
    if dp[diff][n]!=0:
        return dp[diff][n]



    res=2*findsequence(n-1,diff,dp)+findsequence(n-1,diff-1,dp)+findsequence(n-1,diff+1,dp)
    dp[abs(diff)][n]=res
    return res


def findEvenLengthBinarySequence(n):

    dp=[[ 0 for j in range(10)] for i in range(10)]
    dp[0][1]=2
    dp[1][1]=1

    res=findsequence(n,0,dp)
    print(res)
    for i in range(len(dp)):
        print(dp[i])

findEvenLengthBinarySequence(1)
findEvenLengthBinarySequence(2)
findEvenLengthBinarySequence(3)
findEvenLengthBinarySequence(4)


