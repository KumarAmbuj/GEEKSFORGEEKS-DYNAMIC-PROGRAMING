def subsetsum(arr,sum):
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
                    dp[i][j]=(dp[i-1][j] or dp[i-1][j-arr[i-1]])
    print(dp[len(arr)][sum])

set = [3, 34, 4, 12, 5, 2]
sum = 9
subsetsum(set,sum)

set = [3, 34, 4, 12, 5, 2]
sum = 30
subsetsum(set,sum)
