class Common():
    def __init__(self,i,j,psf,l):
        self.i=i
        self.j=j
        self.psf=psf
        self.l=l
def Queue():
    queue=[]
    return queue
def Enqueue(queue,s):
    queue.append(s)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)

def findlrs(s):
    dp=[[0 for j in range(len(s)+1)] for i in range(len(s)+1)]

    for i in range(len(s)-1,-1,-1):
        for j in range(len(s)-1,-1,-1):

            if s[i]==s[j] and i!=j:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])
    print(dp[0][0])
    for i in range(len(dp)):
        print(dp[i])
    findsequence(dp,s)

def findsequence(dp,s):
    queue=Queue()

    Enqueue(queue,Common(0,0,'',dp[0][0]))

    while(Size(queue)):
        rem=Dequeue(queue)

        if rem.l==0:
            print(rem.psf)
        else:
            if s[rem.i] == s[rem.j] and rem.i != rem.j:
                Enqueue(queue, Common(rem.i + 1, rem.j + 1, rem.psf + s[rem.i], rem.l - 1))
            else:
                if dp[rem.i][rem.j] == dp[rem.i][rem.j + 1]:
                    Enqueue(queue, Common(rem.i, rem.j + 1, rem.psf, rem.l))
                if dp[rem.i][rem.j] == dp[rem.i + 1][rem.j]:
                    Enqueue(queue, Common(rem.i + 1, rem.j, rem.psf, rem.l))


s='AABEBCDD'
findlrs(s)