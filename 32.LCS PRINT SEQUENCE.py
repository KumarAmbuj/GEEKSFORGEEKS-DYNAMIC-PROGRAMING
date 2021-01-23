class Common():
    def __init__(self,i,j,psf,l):
        self.i=i
        self.j=j
        self.psf=psf
        self.l=l

def Queue():
    queue=[]
    return queue
def Enqueue(q,s):
    q.append(s)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)

def findsequence(dp,s1,s2):
    queue=Queue()
    Enqueue(queue,Common(0,0,'',dp[0][0]))

    while(Size(queue)):

        rem=Dequeue(queue)


        if rem.l==0:
            print('sequence',rem.psf)

        else:
            if s1[rem.i] == s2[rem.j]:
                Enqueue(queue, Common(rem.i + 1, rem.j + 1, rem.psf + s1[rem.i], rem.l - 1))
            else:
                if dp[rem.i][rem.j] == dp[rem.i + 1][rem.j]:
                    Enqueue(queue, Common(rem.i + 1, rem.j, rem.psf, rem.l))
                if dp[rem.i][rem.j] == dp[rem.i][rem.j + 1]:
                    Enqueue(queue, Common(rem.i, rem.j + 1, rem.psf, rem.l))


def findlcs(s1,s2):
    dp=[[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]

    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):

            if s1[i]==s2[j]:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])
    print('lcs length',dp[0][0])

    findsequence(dp,s1,s2)

A = "AGGTAB"
B = "GXTXAYB"

findlcs(A,B)
