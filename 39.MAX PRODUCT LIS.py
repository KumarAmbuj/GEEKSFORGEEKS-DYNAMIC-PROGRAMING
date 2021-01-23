def findmaxproductlis(arr):

    lis=[1 for i in range(len(arr))]

    for i in range(len(arr)):
        mx=1

        for j in range(i):
            if arr[j]<arr[i]:
                mx=max(mx,lis[j])

        lis[i]=mx*arr[i]

    mx=0
    for i in range(len(arr)):
        mx=max(mx,lis[i])

    print(mx)

arr = [ 10, 22, 9, 33, 21, 50, 41, 60 ]
findmaxproductlis(arr)

arr = [ 3, 100, 4, 5, 150, 6 ]
findmaxproductlis(arr)