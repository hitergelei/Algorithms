'''二维数组中的查找
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个
二维数组和一个整数，判断数组中是否含有该整数。
'''

# 思路：
# 链接：https://www.nowcoder.com/questionTerminal/abc3fe2ce8e146608e868a70efebf62e
# 来源：牛客网

# 利用二维数组由上到下，由左到右递增的规律，
# 那么选取右上角或者左下角的元素a[row][col]与target进行比较，
# 当target小于元素a[row][col]时，那么target必定在元素a所在行的左边,
# 即col--；
# 当target大于元素a[row][col]时，那么target必定在元素a所在列的下边,
# 即row++；
class Solution:
	def Find(self, target, array):
		if array == [[]]:
			return False
		row = 0
		col = len(array[0]) -1 
		while(row <= len(array)-1 and col >= 0):
			if (target == array[row][col]):
				return True
			elif (target > array[row][col]):
				row += 1
			else:
				col -= 1
		return False

array = [[1,2,8,9],
         [2,4,9,12],
         [4,7,10,13],
         [6,8,11,15]]


#print(array[3][3])

s = Solution()
print(s.Find(7,array))

