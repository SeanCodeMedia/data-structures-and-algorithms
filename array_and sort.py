'''
    def sortedSquares(self, nums):
        for index in range(len(nums)):
            nums[index] = nums[index]**2 O(N)

        return sorted(nums) 
ret = print(Solution().sortedSquares([-4,-1,0,3,10])) O(N log N)
'''

class Solution(object):

    def sortedSquares(self, nums):
        low_index = 0
        high_index = len(nums)-1

        for index in nums:

            if abs(nums[high_index]) > abs(nums[low_index]):
                
                nums[high_index] = nums[high_index]**2 
                high_index = high_index - 1
         
            elif abs(nums[high_index]) < abs(nums[low_index]): 

                nums[low_index] = nums[low_index]**2
                low_index = low_index + 1 

        return nums
                

                
ret = print(Solution().sortedSquares([-4,-1,0,3,10]))