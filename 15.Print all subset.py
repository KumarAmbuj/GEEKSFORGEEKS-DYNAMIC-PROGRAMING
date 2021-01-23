class Path:
    def __init__(self,i,j,psf):
        self.i=i
        self.j=j
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

def findsubset(arr,sum):
    dp=[[False for j in range(sum+1)] for i in range(len(arr)+1)]


    for i in range(len(dp)):
        for j in range(len(dp[0])):

            if i==0 and j==0:
                dp[i][j]=True
            elif i==0:
                dp[i][j]=False
            elif j==0:
                dp[i][j]=True

            else:

                if j<arr[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
    print(dp[len(arr)][sum])

    findpath(arr,dp)
def findpath(arr,dp):
    queue=Queue()
    Enqueue(queue,Path(len(arr),len(dp[0])-1,''))

    while(Size(queue)):

        rem=Dequeue(queue)

        if rem.i==0 or rem.j==0:
            print(rem.psf)
        else:
            if dp[rem.i - 1][rem.j]:
                Enqueue(queue, Path(rem.i - 1, rem.j, rem.psf))
            if rem.j - arr[rem.j - arr[rem.i - 1]] >= 0:
                if dp[rem.i - 1][rem.j - arr[rem.i - 1]]:
                    Enqueue(queue, Path(rem.i - 1, rem.j - arr[rem.i - 1], str(arr[rem.i - 1]) + ' ' + rem.psf))


arr = [2, 3, 5, 6, 8, 10]
sum = 10

findsubset(arr,sum)


