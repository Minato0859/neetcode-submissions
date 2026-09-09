class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup_dict = {} # key=int, value=count
        for num in nums:
            if num in lookup_dict:
                lookup_dict[num] += 1
            else:
                lookup_dict[num] = 1
        
        ordered_dict = {k:v for k, v in sorted(lookup_dict.items(), key=lambda item:item[1], reverse =True)}

        return list(ordered_dict.keys())[:k]