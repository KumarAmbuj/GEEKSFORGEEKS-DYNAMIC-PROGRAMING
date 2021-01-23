def findmaxsum(arr):
    maxsofar=0
    maxendinghere=0
    start=0
    end=0
    s=0

    for i in range(len(arr)):
        maxendinghere+=arr[i]

        if maxendinghere>maxsofar:
            maxsofar=maxendinghere
            start=s
            end=i
        if maxendinghere<0:
            maxendinghere=0
            s=i+1

    print(end-start+1)

a = [1, -2, 1, 1, -2, 1]
findmaxsum(a)

a = [-2, -3, 4, -1, -2, 1, 5, -3]
findmaxsum(a)

