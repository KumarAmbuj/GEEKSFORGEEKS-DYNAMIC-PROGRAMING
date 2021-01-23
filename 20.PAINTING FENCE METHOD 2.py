def paintingfence(n,k):
    same=k
    diff=k*(k-1)
    sum=same+diff

    for i in range(3,n+1):
        same=diff
        diff=sum*(k-1)
        sum=same+diff

    print(sum)

paintingfence(2,4)