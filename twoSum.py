class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        
        for idx, item in enumerate(nums):
            counter_part = target - item
            if counter_part in hash_table:
                return [hash_table[counter_part], idx]
            else:
                hash_table[item] = idx
        return []