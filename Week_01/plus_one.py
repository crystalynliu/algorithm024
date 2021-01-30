# 1. recursion

# Time complexity ?
# Space complexity O(1)

class Solution1:
  def plusOne(self, digits: List[int]) -> List[int]:
    others, lastNum = digits[:-1], digits[-1]
    lastNum = (lastNum + 1) % 10

    if lastNum == 0:
      if len(others) == 0:
        return [1, 0]
      return self.plusOne(others) + [0]
    return others + [lastNum]

# Question: how to calculate the time complexity for above solution?

# 2. loop

# Time complexity O(n)
# Space complexity O(1)

class Solution2:
  def plusOne(self, digits: List[int]) -> List[int]:
    for i in range(len(digits), -1, -1):
      digits[i] = (digits[i] + 1) % 10
      if digits[i] != 0:
        return digits
    return [1] + digits

