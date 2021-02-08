class Solution:
  def isUgly(self, num: int) -> bool:
    if num <= 0: return False
    for n3 in [2,3,5]:
      while num % n3 == 0:
        num //= n3
    return num == 1
