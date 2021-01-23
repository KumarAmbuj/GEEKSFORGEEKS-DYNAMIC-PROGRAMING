def paintingfence(n,k):
    same=[0 for i in range(n+1)]
    diff=[0 for i in range(n+1)]
    sum=[0 for i in range(n+1)]

    same[2]=k
    diff[2]=k*(k-1)
    sum[2]=same[2]+diff[2]

    for i in range(3,n+1):
        same[i]=diff[i-1]
        diff[i]=sum[i-1]*(k-1)
        sum[i]=same[i]+diff[i]

    print(sum[n])

paintingfence(2,4)

paintingfence(3,2)

