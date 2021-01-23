class Sequence():
    def __init__(self,i,l,psf):
        self.i=i
        self.l=l
        self.psf=psf

def Queue():
    queue=[]
    return queue
def Enqueue(queue,s):
    queue.append(s)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)


def printlis(arr):
    dp=[0 for i in range(len(arr))]

    for i in range(len(arr)):
        mx=0
        for j in range(i):
            if arr[j]<arr[i]:
                mx=max(mx,dp[j])

        dp[i]=mx+1
    mx=0
    for i in range(len(dp)):
        mx=max(mx,dp[i])

    print(mx)
    findsequence(dp,arr,mx)

def findsequence(dp,arr,mx):
    queue=Queue()
    for i in range(len(arr)):
        if dp[i]==mx:
            Enqueue(queue,Sequence(i,mx,str(arr[i])))
    while(Size(queue)):
        rem=Dequeue(queue)

        if rem.l==1:
            print(rem.psf)
        else:

            for j in range(rem.i):
                if dp[j]==rem.l-1 and arr[j]<arr[rem.i]:
                    Enqueue(queue,Sequence(j,rem.l-1,str(arr[j])+' '+rem.psf))

arr=[10,22,9,33,21,50,41,60,80,3]
printlis(arr)
