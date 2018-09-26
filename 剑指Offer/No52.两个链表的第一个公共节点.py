"""
题目：输入两个链表，找出它们的第一个公共节点。
"""
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def findFirstCommonNode(self, pHead1, pHead2):