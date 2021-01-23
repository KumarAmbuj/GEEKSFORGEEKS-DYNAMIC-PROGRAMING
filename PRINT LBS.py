class Sequence():
    def __init__(self,si,l,i,psf,flag):
        self.si=si
        self.l=l
        self.i=i
        self.psf=psf
        self.flag=flag

def Queue():
    queue=[]
    return queue
def Enqueue(q,s):
    q.append(s)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)

def findLbsSequence(arr):
    lis=[0 for i in range(len(arr))]
    lds=[0 for j in range(len(arr))]

    #for lis

    for i in range(len(arr)):
        mx=0

        for j in range(i):
            if arr[j]<arr[i]:
                mx=max(mx,lis[j])
        lis[i]=mx+1

    # for lds
    for i in range(len(arr)-1,-1,-1):
        mx=0

        for j in range(len(arr)-1,i,-1):
            if arr[j]<arr[i]:
                mx=max(mx,lds[j])
        lds[i]=mx+1


    mx = 0

    for i in range(len(arr)):
        mx = max(mx,lis[i] + lds[i] - 1)
    print(mx)
    findsequence(lis,lds,arr)



def findsequence(lis,lds,arr):
    mx = 0

    for i in range(len(arr)):
        mx = max(mx,lis[i] + lds[i] - 1)

    queue=Queue()

    for i in range(len(arr)):
        if lis[i]+lds[i]==mx+1:
            Enqueue(queue,Sequence(i,lis[i],i,str(arr[i]),False))


    while(Size(queue)):
        rem=Dequeue(queue)
        if rem.l==1 and rem.flag==False:
            Enqueue(queue,Sequence(rem.si,lds[rem.si],rem.si,rem.psf,True))
        if rem.l==1 and rem.flag==True:
            print(rem.psf)

        elif rem.flag==False:
            for j in range(rem.i):
                if lis[j]==rem.l-1 and arr[j]<arr[rem.i]:
                    Enqueue(queue,Sequence(rem.si,rem.l-1,j,str(arr[j])+' '+rem.psf,False))


        elif rem.flag==True:
            for j in range(len(arr)-1,rem.i,-1):
                if lds[j]==rem.l-1 and arr[j]<arr[rem.i]:
                    Enqueue(queue,Sequence(rem.si,rem.l-1,j,rem.psf+' '+str(arr[j]),True))


arr = [1, 15, 51, 45, 33,
                   100, 12, 18, 9]
findLbsSequence(arr)






