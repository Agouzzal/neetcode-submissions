class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]]+=1
            else:
                seen[nums[i]]=1
        sor=sorted(seen.items(), key=lambda p :p[1],reverse=True)
        ma_list = [pair[0] for pair in sor][:k]
        return ma_list


        