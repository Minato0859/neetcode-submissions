class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup_dict = {} # key=int, value=count
        for num in nums:
            if num in lookup_dict:
                lookup_dict[num] += 1
            else:
                lookup_dict[num] = 1
        
        ordered_list_tuples = sorted(lookup_dict.items(), key=lambda item:item[1], reverse =True)

        return [tuples[0] for tuples in ordered_list_tuples[0:k]]