## moves zero
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
