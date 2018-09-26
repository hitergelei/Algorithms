'''
输入一个链表，从尾到头反过来打印出每个节点的值。
'''
class ListNode:
	def __init__(self, x = None):
		self.val = x
		self.next = None

class Solution:
	def printListFromTailToHead(self, listNode):		
		lis = []
		head = listNode

		while head :  #while head is not None 
			#list.insert(index, obj)
			#index -- 对象 obj 需要插入的索引位置。
			lis.insert(0, head.val)
			head = head.next
		return lis

#更健硕的写法
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         # write code here
#         if not listNode:
#             return []
#         lis = []
#         while listNode: #while listNode is not None
#             lis.insert(0, listNode.val)
#             listNode = listNode.next
#         return lis

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)   #输入的链表只有一个节点
test = ListNode()   #输入的链表头节点为空节点（为空链表）

s = Solution()
print(s.printListFromTailToHead(node1))
print(s.printListFromTailToHead(node2))
print(s.printListFromTailToHead(test))
print(s.printListFromTailToHead(singleNode))
print(s.printListFromTailToHead({}))  #输入的是字典类型，打印出[]






