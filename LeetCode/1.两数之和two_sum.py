'''
题目：
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

> 示例：

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
class Solution:
    def twoSum(self, nums, target):     # 第一个数+ 第二个数  = target
        seen = { }
        for index, num in enumerate(nums):
            key = target - num   

            if key in seen: 
               return[seen[key], index]   #返回第一个数的索引和第二个数的索引
            else:
                seen[num] = index   #sen字典存放第一个数以及其在nums中的索引
        

        return [ ]

a = [1,2,4,5,6]
s= Solution()
s.twoSum(a,6)

'''
注意：对于字典的这种方式，如果我们只是判断 i 以及 target - i 是不是相等，
这样是错误的，如果两个元素相同，但是不是同一个元素，那就会出错了

复杂度分析：

时间复杂度：O(n)O(n)， 我们只遍历了包含有 nn 个元素的列表一次。在表中进行的每次查找只花费 O(1)O(1) 的时间。

空间复杂度：O(n)O(n)， 所需的额外空间取决于哈希表中存储的元素数量，该表最多需要存储 nn 个元素。
'''
