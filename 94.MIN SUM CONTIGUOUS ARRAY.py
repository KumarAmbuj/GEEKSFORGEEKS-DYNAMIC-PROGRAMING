def findminsum(arr):
    minendinghere=0
    minsofar=10000

    for i in range(len(arr)):
        minendinghere+=arr[i]

        if minendinghere<minsofar:
            minsofar=minendinghere

        if minendinghere>0:
            minendinghere=0

    print(minsofar)

arr = [3, -4, 2, -3, -1, 7, -5]
findminsum(arr)