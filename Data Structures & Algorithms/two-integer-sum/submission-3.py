class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_hash = dict()
        for i in range(0, len(nums)):
            cal_difference = target - nums[i]
            if cal_difference in lookup_hash:
                return sorted([i, lookup_hash.get(cal_difference)]) #update to reorder properly
            else:
                lookup_hash[nums[i]] = i # lookup_hash = {key = nums, index of nums}
            

