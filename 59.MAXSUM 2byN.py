def findmaxsum(arr):
    inc=max(arr[0][0],arr[1][0])
    exc=0

    for i in range(1,len(arr[0])):
        ninc=exc+max(arr[0][i],arr[1][i])
        nexc=max(inc,exc)

        inc=ninc
        exc=nexc

    ans=max(inc,exc)
    print(ans)
grid = [ [ 1, 2, 3, 4, 5],
             [ 6, 7, 8, 9, 10] ]
findmaxsum(grid)