def findlargestsum(arr):

    maxendinghere=0
    maxsumsofar=0

    for i in range(len(arr)):
        maxendinghere+=arr[i]
        if maxendinghere>maxsumsofar:
            maxsumsofar=maxendinghere

        elif maxendinghere<0:
            maxendinghere=0

    print(maxsumsofar)

a = [-2, -3, 4, -1, -2, 1, 5, -3]
findlargestsum(a)