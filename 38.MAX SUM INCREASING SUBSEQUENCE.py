def findmaxsumlis(arr):
    lis=[0 for i in range(len(arr))]

    for i in range(len(lis)):
        mx=0

        for j in range(i):

            if arr[j]<arr[i]:
                mx=max(mx,lis[j])
        lis[i]=mx+arr[i]

    mx=0
    for i in range(len(arr)):
        mx=max(mx,lis[i])

    print(mx)
arr = [1, 101, 2, 3, 100, 4, 5]
findmaxsumlis(arr)