def findmaxdiff(s):
    maxendinghere=0
    maxsofar=0

    for i in range(len(s)):
        maxendinghere+=(1 if s[i]=='0' else -1)

        if maxendinghere>maxsofar:
            maxsofar=maxendinghere

        if maxendinghere<0:
            maxendinghere=0
    print(maxsofar)

s = "11000010001"
findmaxdiff(s)