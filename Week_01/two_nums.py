# 1. Double loop

# Time complexity O(n^2)
# Space complexity O(1)

class Solution1:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
          return [i, j]


# 2. Single loop with dictionary

# Time complexity O(n^2) or O(n) ?
# Space complexity O(1)

class Solution2:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    store = {}
    for index, num in enumerate(nums):
      complement = target - nums
      if complement in store:
        return [store[complement], index]
      store[num] = index

# Question:
# what's the time complexity for `if a in dict`?
