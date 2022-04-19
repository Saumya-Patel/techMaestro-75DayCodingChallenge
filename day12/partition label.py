class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dicti={}
        i=0
        while (i < len(s)):
            if s[i] not in dicti:
                dicti[s[i]]=i
            else:
                dicti[s[i]]=i
            i+=1
        i=0
        ans=[]
        temp=0
        while(i<len(s)):
            temp=dicti[s[i]]
            j=0
            while(i+j<=temp):
                if(dicti[s[i+j]]>temp):
                    temp=dicti[s[i+j]]
                j+=1
            ans.append(j)
            i=i+j
        return ans
