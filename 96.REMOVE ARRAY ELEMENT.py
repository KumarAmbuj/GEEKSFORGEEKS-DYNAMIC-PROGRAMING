def maxvalue(arr,low,high,turn,dp):
    if low==high:
        return arr[low]*turn

    if dp[low][high]!=0:
        return dp[low][high]



    dp[low][high]=max(arr[low]*turn+maxvalue(arr,low+1,high,turn+1,dp),arr[high]*turn+maxvalue(arr,low,high-1,turn+1,dp))
    for i in range(len(dp)):
        print(dp[i])
    print()
    return dp[low][high]

def findmaxvalue(arr):
    low=0
    high=len(arr)-1
    turn=1

    dp=[[0 for i in range(len(arr))] for j in range(len(arr))]

    ans=maxvalue(arr,low,high,turn,dp)
    print(ans)
    for i in range(len(dp)):
        print(dp[i])

arr = [ 1, 3, 1, 5, 2 ]
findmaxvalue(arr)
