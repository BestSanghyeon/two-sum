from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
  for i, a in enumerate(nums):
    for j, b in enumerate(nums[i+1:]):
      if a + b == target:
        return [i, j+i+1]
  return
