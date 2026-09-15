#with sorting
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for i in range(len(strs)):
            sor ="".join(sorted(strs[i]))
            if sor in seen:
                seen[sor].append(strs[i])
            else:
                seen[sor]=[strs[i]]
        return list(seen.values())
            
