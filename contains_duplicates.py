class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # O(N)T and O(N)s

        my_set = set()

        for x in range(len(nums)):

            if nums[x] in my_set:
                return True
            else:
                my_set.add(nums[x])

        return False


