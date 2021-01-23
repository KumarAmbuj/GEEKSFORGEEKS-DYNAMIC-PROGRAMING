def findsubsetsum(arr,sum):
    dp=[[False for j in range(sum+1)] for i in range(2)]

    for i in range(len(arr)+1):
        for j in range(sum+1):
            if j==0:
                dp[i%2][j]=True
            elif i==0:
                dp[i%2][j]=False
            elif j<arr[i-1]:
                dp[i%2][j]=dp[(i+1)%2][j]
            else:
                dp[i%2][j]=dp[(i+1)%2][j] or dp[(i+1)%2][j-arr[i-1]]
    for i in range(2):
        print(dp[i])
    print(dp[len(arr)%2][sum])

arr = [ 6, 2, 5 ]
sum = 11
findsubsetsum(arr,sum)

arr = [ 6, 2, 5 ]
sum = 9
findsubsetsum(arr,sum)