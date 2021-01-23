def partition(arr,p,r):
    x=arr[r]
    i=p-1

    for j in range(p,r):
        if arr[j]<x:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)


def LargestPairSubset(arr):

    Quicksort(arr,0,len(arr)-1)


    dp=[0 for i in range(len(arr))]

    for i in range(len(arr)-1,-1,-1):
        mx=0

        for j in range(len(arr)-1,i,-1):

            if arr[j]%arr[i]==0:
                if mx<dp[j]:
                    mx=dp[j]
        dp[i]=mx+1

    mx=0
    for i in range(len(dp)):
        mx=max(mx,dp[i])
    print(mx)
arr=[10,5,3,15,20]
LargestPairSubset(arr)