'''
题目：两数相加  (难度：中等)
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。
将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例： 
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
'''
思路：
本题的思路很简单，按照小学数学中学习的加法原理从末尾到首位，对每一位对齐相加即可。
技巧在于如何处理不同长度的数字，以及进位和最高位的判断。将两个单链表表示的数字相加，再将结果用单链表表示出来。
主要考察对链表的操作，对链表这种数据结构的遍历、增、删等操作应该熟练。
'''
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
		if not l1:
			return l2
		if not l2:
			return l1

		val1, val2 = [l1.val], [l2.val]

		while l1.next:
			val1.append(l1.next.val)
			l1 = l1.next
			
		while l2.next:
			val2.append(l2.next.val)
			l2 = l2.next

        # 如：str(0) = '2'
		num1 = ''.join([str(i) for i in val1[::-1]])  #列表val1的[2,4,3]反向并str格式化为字符串形式:'342'
		# print(num1 == '342')
		num2 = ''.join([str(i) for i in val2[::-1]])  #列表val2的[5,6,4]反向并格式化为字符串形式:'465'
        
		tmp = str(int(num1) + int(num2))[::-1]   # 807格式化为字符串并反向，得到字符串tmp = '708'
		res = ListNode(int(tmp[0]))  # 如：res此时包括以后都是链表表头-head，指向第一个节点。res = ListNode(7)
		run_res = res   # run_res刚开始是指向第一个节点  # run_res.val = 7
		for i in range(1, len(tmp)):
			run_res.next = ListNode(int(tmp[i]))
			run_res = run_res.next
		# print(res.val, res.next.val, res.next.next.val)	输出7 0 8
		return res


# 测试
if __name__ == '__main__':
    # 创建对象Solution
    sol = Solution()
    # 定义l1链表
    l1 = ListNode('2')
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    # 定义l2链表
    l2 = ListNode(5)
    l2.next =  ListNode(6)
    l2.next.next =ListNode(4)
    # 获取返回值的链表
    res = sol.addTwoNumbers(l1, l2)
    print(res.val, res.next.val, res.next.next.val)
    
