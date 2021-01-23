def findmaxStolenHouses(arr):
    inc=arr[0]
    exc=0

    for i in range(1,len(arr)):
        ninc=exc+arr[i]
        nexc= max(inc,exc)

        inc=ninc
        exc=nexc

    ans=max(inc,exc)
    print(ans)

hval = [6, 7, 1, 3, 8, 2, 4]
findmaxStolenHouses(hval)

hval = [5, 3, 4, 11, 2]
findmaxStolenHouses(hval)