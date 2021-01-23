def findmaxsum(arr,k):
    n=len(arr)
    maxendinghere=0
    maxsofar=0

    for i in range(len(arr)*k):
        maxendinghere+=arr[i%n]

        if maxendinghere>maxsofar:
            maxsofar=maxendinghere

        if maxendinghere<0:
            maxendinghere=0

    print(maxsofar)

arr = [-1, 10, 20]
findmaxsum(arr,2)
