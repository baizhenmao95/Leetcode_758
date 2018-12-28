# --coding: utf-8 --
'''
算法如下：
首先判断是否全非正，若是，则取其最大项
若否，则
先初始化变量，
然后从第一个非负项开始，累加，每加一项，判断sum是否变大，若是，更新该值（temp1）,同时记录正着加的数组长度
然后将数组反向，再从第一个非负项开始累加，记录和最大的时刻（temp2）
输出temp1与temp2中较大的那个

'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        sum = nums[0]
        maxm = nums[0]
        n = 0
        temp1 = 0
        temp2 = 0
        for num in nums:
            if num > maxm:
                maxm = num

        if maxm <= 0:
            temp1 = maxm
            temp2 = temp1
        else:
            sum = 0
            for i in range(ln):
                if nums[i] <= 0:
                    continue
                if nums[i]>0:
                    for j in range(i,ln):
                        sum += nums[j]
                        n += 1
                        if temp1 < sum:
                            temp1 = sum
                        if sum<0:
                            sum = 0
#                            n = 0
                            continue
                    break

            if n != 0:
                newnums = nums[:-n-1:-1]
                lnn = len(newnums)
                sum = 0
                for i in range(lnn):
                    if newnums[i]>0 & sum==0:
                        for j in range(i,lnn):
                            sum += newnums[j]
                            if temp2 < sum:
                                temp2 = sum
                            if sum<0:
                                sum = 0
                                continue
                        break

        return max(temp1, temp2)

nums = [-1]
# nums = [1,-1,-2]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
a = Solution()
s = a.maxSubArray(nums)
print(s)
