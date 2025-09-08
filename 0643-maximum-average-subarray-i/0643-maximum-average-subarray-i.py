class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        intial = 0
        pointr = k
        big_sum = sum(nums[:k])
        sums = big_sum
        length = len(nums)
        while(pointr < length):
            sums = sums + nums[pointr] - nums[intial]
            if sums > big_sum:
                big_sum = sums
            pointr = pointr+1
            intial = intial+1    
        return float(big_sum)/k  
        