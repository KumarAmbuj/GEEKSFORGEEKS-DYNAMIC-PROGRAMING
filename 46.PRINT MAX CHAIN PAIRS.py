class Chain:
    def __init__(self,f,s):
        self.f=f
        self.s=s
class Sequence():
    def __init__(self,l,i,psf):
        self.l=l
        self.i=i
        self.psf=psf

def Queue():
    queue=[]
    return queue
def Enqueue(q,s):
    q.append(s)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)


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
    for i in range(len(arr)):
        mx=max(mx,dp[i])

    return mx,dp

def findsequence(l,dp,arr):
    queue=Queue()
    for i in range(len(dp)):
        if dp[i]==l:
            Enqueue(queue,Sequence(l,i,"("+str(arr[i].f)+", "+str(arr[i].s)+")"))
    while(Size(queue)):

        rem=Dequeue(queue)
        if rem.l==1:
            print(rem.psf)
        else:
            for j in range(rem.i):
                if dp[j]==rem.l-1 and arr[j].s<arr[rem.i].f:
                    Enqueue(queue,Sequence(rem.l-1,j,"("+str(arr[j].f)+", "+str(arr[j].s)+")"+" "+rem.psf))


def findmaxchain(chain):
    arr=[]
    for i in range(len(chain)):
        arr.append(Chain(chain[i][0],chain[i][1]))

    Quicksort(arr,0,len(arr)-1)

    l,dp=findlis(arr)

    findsequence(l,dp,arr)

arr=[(5, 24), (39, 60), (15, 28), (27, 40), (50, 90)]
findmaxchain(arr)
