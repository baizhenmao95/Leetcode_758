
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
               if target - nums[i] == nums[j]:
                    return(i,j)
                    break


nums = [3,2,4]
target = 6
a = Solution()
s = a.twoSum(nums,target)
s = list(s)
print(s,type(s))
