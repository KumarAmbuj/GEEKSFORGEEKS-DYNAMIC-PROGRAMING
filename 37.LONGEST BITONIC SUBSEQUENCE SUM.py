def findLBSsum(arr):
    lis=[0 for i in range(len(arr))]
    lds=[0 for j in range(len(arr))]

    #for lis

    for i in range(len(arr)):
        mx=0

        for j in range(i):
            if arr[j]<arr[i]:
                mx=max(mx,lis[j])

        lis[i]=mx+arr[i]

    # for lds

    for i in range(len(arr)-1,-1,-1):
        mx=0

        for j in range(len(arr)-1,i,-1):

            if arr[j]<arr[i]:

                mx=max(mx,lds[j])
        lds[i]=mx+arr[i]


    mx=0

    for i in range(len(arr)):
        mx=max(mx,lis[i]+lds[i]-arr[i])

    print(mx)


arr = [1, 15, 51, 45, 33, 100, 12, 18, 9]
findLBSsum(arr)

arr = [80, 60, 30, 40, 20, 10]
findLBSsum(arr)