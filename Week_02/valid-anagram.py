class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if set(s) == set(t):
      for char in set(s):
        flag = s.count(char) == t.count(char)
        if not flag: return False
      else:
        return True
    else:
      return False
