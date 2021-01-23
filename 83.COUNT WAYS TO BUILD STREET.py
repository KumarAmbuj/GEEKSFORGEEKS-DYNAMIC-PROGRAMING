def buildstreet(n):
    choice1=[0 for i in range(n+1)]
    choice2=[0 for i in range(n+1)]


    choice1[1]=1
    choice2[1]=2

    for i in range(2,n+1):
        choice1[i]=choice1[i-1]+choice2[i-1]
        choice2[i]=2*choice1[i-1]+choice2[i-1]

    ans=choice1[n]+choice2[n]

    print(ans)


buildstreet(2)
buildstreet(3)
buildstreet(4)
buildstreet(5)