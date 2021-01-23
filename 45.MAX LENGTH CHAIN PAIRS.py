class Chain:
    def __init__(self,f,s):
        self.f=f
        self.s=s
def partition(arr,p,r):
    x=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j].f<x.f:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1
def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)

def findlis(arr):
    dp=[0 for i in range(len(arr))]

    for i in range(len(arr)):
        mx=0
        for j in range(i):
            if arr[j].s<arr[i].f:
                mx=max(mx,dp[j])
        dp[i]=mx+1

    mx=0
    for i in range(len(dp)):
        mx=max(mx,dp[i])
    return mx
def maxLenChainPairs(chain):

    arr=[]

    for i in range(len(chain)):
        arr.append(Chain(chain[i][0],chain[i][1]))

    Quicksort(arr,0,len(arr)-1)


    ans=findlis(arr)
    print(ans)
arr=[[5, 24], [39, 60], [15, 28], [27, 40], [50, 90] ]
maxLenChainPairs(arr)


