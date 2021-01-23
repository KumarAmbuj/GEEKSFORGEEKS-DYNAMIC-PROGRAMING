def findmincost(arr,w):
    arr.insert(0,0)
    dp=[-1 for i in range(w+1)]
    dp[0]=0

    for i in range(1,w+1):
        mn=99

        for j in range(1,len(arr)):

            if (i-j)>=0 and arr[j]!=-1 and dp[i-j]!=-1:
                mn=min(mn,dp[i-j]+arr[j])

        if mn!=99:
            dp[i]=mn
        else:
            dp[i]=-1

    print(dp[w])


W = 5
cost = [20, 10, 4, 50, 100]
findmincost(cost,W)

W = 5
cost = [-1, -1, 4, 5, -1]
findmincost(cost,W)

W = 5
cost = [1,2,3, 4, 5]
findmincost(cost,W)


