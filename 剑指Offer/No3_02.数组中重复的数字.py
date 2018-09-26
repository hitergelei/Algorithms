'''
题目二： 
在一个长度为n+1的数组里的所有数字都在1~n的范围内，所以数组中至少有一个数字是重复的。
请找出数组中任意一个重复的数字，但是不能修改输入的数组。
例如，如果输入长度为8的数组{2,3,5,4,3,2,6,7}，那么对应的输出是重复的数字2或者3。
'''

class Solution:
	#二分法查找，用时间换空间，提高算法空间效率。 时间nlogn,空间O(1)
	def getDuplication(self, numbers):
		if numbers == None or len(numbers)  <= 0:
			return -1

		# start相当于left, end相当于right
		start = 1
		end = len(numbers) - 1
		while end >= start:
			middle = start + ((end - start) >> 1)
			print("middle = ",middle)
			print("numbers[middle] = ", numbers[middle])
			count = self.countRange(numbers, start, middle)
			print("count = ",count)
			if end == start:
				if count > 1:
					return start
				else:
					break
			if count > (middle - start + 1):
				end = middle
			else:
				start = middle + 1
		
		return start

	def countRange(self, numbers, start, mid):
		if numbers == None:
			return 0
		#count = 0
		# for item in numbers:
		# 	if start <= item and item <= mid:
		# 		count += 1
		# return count
		count = 0
		for i in range(len(numbers)): 

			if numbers[i] >= start and numbers[i] <= mid:
				count =count + 1
		return count

# class Solution:
# 	def count(self, nums, left, right):
# 	    total = 0
# 	    for item in nums:
# 	        if item >= left and item <= right:
# 	            total += 1
# 	    return total

# 	def getDuplication(self, nums):
# 	    if len(nums) <= 1:
# 	        return False
# 	    n = len(nums)-1
# 	    left = 1
# 	    right = n
# 	    while left < right:
# 	        mid = left + right >> 1
# 	        total = self.count(nums, left, mid)
# 	        if total > mid - left + 1:
# 	            right = mid
# 	        else:
# 	            left = mid + 1
# 	    return left

#测试
a = [2,3,5,4,3,2,6,7]
s = Solution()
res = s.getDuplication(a)
print(res)  #输出为3




