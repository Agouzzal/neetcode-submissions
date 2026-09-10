#Case with one dicts 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s)!=len(t):
            return False
        b={}

        for chara in s:
            if chara in b:
                b[chara]+=1
            else:
                b[chara]=1
                
        for charac in t:
            if charac not in b:
                return False
            else:
                b[charac]-=1
                if b[charac] <0:
                    return False
        return True


        