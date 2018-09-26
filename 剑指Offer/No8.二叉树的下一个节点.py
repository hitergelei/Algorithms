'''
给定一个二叉树和其中的一个结点，如何找出中序遍历顺序的下一个结点并且返回？
注意，树中的结点不仅包含分别指向左、右子节点的指针，还有一个指向父结点的指针。
'''
class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None  #指向父节点的指针

class Solution:
	def GetNext(self, pNode):
		#write code here
		if pNode == None:
			return
		pNext = None
		if pNode.right != None:
			pRight = pNode.right
			while pRight.left != None:
				pRight = pRight.left
			pNext = pRight
        #父节点不为空时
		elif pNode.next != None:
			pCurrent = pNode
			pParent = pCurrent.next
			while pParent != None and pCurrent == pParent.right:
				pCurrent = pParent
				pParent = pParent.next
			pNext = pParent
		return pNext


