def findmintime(a,t,e,x):
    n=len(a[0])
    dp1=[0 for i in range(n)]
    dp2=[0 for i in range(n)]

    dp1[0]=a[0][0]+e[0]

    dp2[0]=a[1][0]+e[1]


    for i in range(1,n):

        dp1[i]=min(dp1[i-1]+a[0][i],dp2[i-1]+t[1][i]+a[0][i])
        dp2[i]=min(dp2[i-1]+a[1][i],dp1[i-1]+t[0][i]+a[1][i])

    ans=min(dp1[n-1]+x[0],dp2[n-1]+x[1])
    print(ans)


a = [[4, 5, 3, 2],
     [2, 10, 1, 4]]

t = [[0, 7, 4, 5],
     [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]

findmintime(a,t,e,x)