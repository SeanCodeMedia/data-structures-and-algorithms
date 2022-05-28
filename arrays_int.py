
class Solution(object):


	def findNumbers(self, nums):

		even_numbers_counter = 0

		for number in nums:
			number_length = len(str(number))
			if number_length % 2 == 0: 
				even_numbers_counter += 1 
				print(str(number) + " contains " + str(number_length) +" digits (even number of digits) " )
			else: 
				print(str(number) + " contains " + str(number_length) +" digits (odd number of digits) " )
		return even_numbers_counter 






ret = Solution().findNumbers([555,901,482,1771])

		