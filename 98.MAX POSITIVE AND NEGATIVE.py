def findmaxvalue(arr):
    dp=[0 for i in range(len(arr))]
    dp[len(arr)-1]=1
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>0:
            if arr[i+1]<0:
                dp[i]=dp[i+1]+1
            else:
                dp[i]=1
        elif arr[i]<0:
            if arr[i+1]>0:
                dp[i]=dp[i+1]+1
            else:
                dp[i]=1


    for i in range(len(arr)):
        print('index ',i,dp[i])

arr=[-5, -1, -1, 2, -2, -3]
findmaxvalue(arr)
print()
arr=[1, -5, 1, -5]
findmaxvalue(arr)

