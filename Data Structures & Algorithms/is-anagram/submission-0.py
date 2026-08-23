class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts={}
        countj={}
        for i in s:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        for j in t:
            if j in countj:
                countj[j]+=1
            else:
                countj[j]=1
        if counts==countj:
            return True
        else:
            return False
