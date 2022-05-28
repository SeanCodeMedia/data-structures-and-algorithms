class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
         
        counter = 0
        max_amount = 0

        for x in range(len(nums)):
            if nums[x] == 1:
                counter += 1 
            elif nums[x] == 0:
                if max_amount < counter:
                    max_amount = counter
                counter = 0
            if x == len(nums)-1:
                if max_amount < counter:
                    max_amount = counter
                counter = 0
        return max_amount


                

            
        

        """
        :type nums: List[int]
        :rtype: int
        """

mysolution = Solution().findMaxConsecutiveOnes([1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0])

print(mysolution)