class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # complement of num : indice of num
        my_dict = {}
        for idx in range(len(nums)):
            if nums[idx] in my_dict:
                return [my_dict[nums[idx]], idx]
            else:
                my_dict[target - nums[idx]] = idx
