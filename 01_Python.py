from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    a.append(i)
                    a.append(j)
                    print(a)
                    break
                else:
                    continue        
        return a
s = Solution()
s.twoSum(nums = [10,22,31,12,20], target= 32)