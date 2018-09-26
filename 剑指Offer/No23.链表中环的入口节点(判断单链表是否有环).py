"""
题目：给一个链表，若其中包含环，请找出该链表的环的入口节点，否则，输出null
"""
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def EntryNodeOfLoop(self, pHead):
		if pHead == None or pHead.next == None or pHead.next.next == None:
			return None
		# 使用快慢指针，low每次走一步，fast每次走两步
		low = pHead.next
		fast = pHead.next.next

		# 第一次循环，直到low和fast相遇，low每次走一步，fast每次走两步
		while low != fast:
			# 如果快指针提前遇到了结尾，直接返回null,不可能有环
			if fast.next == None or fast.next.next == None:
				return None
			low = low.next
			fast = fast.next.next

		# 当两者相遇后，跳出前面的while循环，让fast快指针回到开始的头结点
		fast = pHead
		while low != fast:  # 之后low和fast每次都只走一步
			low = low.next
			fast = fast.next
		return fast   # 这里返回的是入口节点的内存地址。如果是返回入口节点的元素，则这里应该是return fast.val

if __name__ == '__main__':
	s = Solution()
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	head.next.next.next.next = ListNode(5)
	head.next.next.next.next.next = ListNode(6)
	head.next.next.next.next.next.next = head.next.next
	print(s.EntryNodeOfLoop(head).val)

"""
假设从链表头节点到入环点的距离是D，链表的环长是S。那么循环会进行S次（
为什么是S次，有心的同学可以自己揣摩下），可以简单理解为O（N）。除了两个指针以外，没有使用任何额外存储空间，
所以空间复杂度是O（1）。
https://blog.csdn.net/u010983881/article/details/78896293
"""