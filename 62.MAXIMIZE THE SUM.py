def findmaxsum(arr):
    hash={i:0 for i in range(len(arr)+1)}

    for i in range(len(arr)):
        hash[arr[i]]+=1


    maxi=max(arr)

    for i in range(2,maxi+1):
        hash[i]=max(hash[i-1],hash[i-2]+hash[i]*i)
    print(hash[maxi])


a = [1, 2, 3]
findmaxsum(a)
a = [1, 2, 2,2,3,4]
findmaxsum(a)


