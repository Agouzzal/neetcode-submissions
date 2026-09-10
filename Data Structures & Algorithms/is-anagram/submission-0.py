#Case with two dicts 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s)!=len(t):
            return False
        b={}
        d={}
        for chara in s:
            if chara in d:
                d[chara]+=1
            else:
                d[chara]=1
                
        for charac in t:
            if charac in b:
                b[charac]+=1
            else:
                b[charac]=1
        return b==d
            


        