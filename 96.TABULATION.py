def findmaxvalue(arr):
    dp=[[0 for i in range(len(arr))]for j in range(len(arr))]

    for g in range(len(arr)):
        i=0
        j=g
        turn=g+1

        while(j<len(arr)):

            if g==0:
                dp[i][j]=arr[i]

            else:
                dp[i][j]=max(arr[i]*turn+dp[i+1][j],arr[j]*turn+dp[i][j-1])
            i+=1
            j+=1
    print(dp[0][len(arr)-1])
arr = [ 1, 3, 1, 5, 2 ]
findmaxvalue(arr)
