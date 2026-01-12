def Validanagram(S,T):
    disctS={}
    for i in S:
        if i in disctS:
            disctS[i]+=1
        else:
            disctS[i]=1
    disctT={}
    for i in T:
        if i in disctT:
            disctT[i]+=1
        else:
            disctT[i]=1
    return disctT==disctS
S="anagram"
T="nagraam"
print(Validanagram(S,T))


