from typing import List
class Solution(object):
    global targetvalues
    targetvalues=[]
    def twoSum(self, nums:List[int] , target:int)  -> List[int]:
      #       """
      #   :type nums: List[int]
      #   :type target: int
      #   :rtype: List[int]
      #   """
            for i in nums:
                  for j in nums:
                        if i!=j and i+j == target:
                              print(f"Values adding upto target are {nums.index(i)} and {nums.index(j)}")
                              targetvalues.append(nums.index(i))
                              targetvalues.append(nums.index(j))
                              print(targetvalues)
                              break
                  else:
                                continue
            return targetvalues

s= Solution()
s.twoSum(nums=[10,20,34,4,5],target=39)

# nums = [1,2,3,4]
# # print(nums.index(1))
# target = 5
# for i in range (1,5):
#       for j in range (1,5):
#             if i+j == target:
#                   print(f"Target is addition of {nums.index(i)} and {nums.index(j)}")

