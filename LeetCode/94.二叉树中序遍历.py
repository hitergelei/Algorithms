"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial（无关紧要）, could you do it iteratively（迭代）?
"""
'''
题目要求用迭代法
根据中序遍历的顺序，对于任一结点，优先访问其左孩子，而左孩子结点又可以看做一根结点，
然后继续访问其左孩子结点，直到遇到左孩子结点为空的结点才进行访问，然后按相同的规则访问其右子树。因此其处理过程如下：

对于任一结点P，

(1)若其左孩子不为空，则将P入栈并将P的左孩子置为当前的P，然后对当前结点P再进行相同的处理；

(2)若其左孩子为空，则取栈顶元素并进行出栈操作，访问该栈顶结点，然后将当前的P置为栈顶结点的右孩子；

(3)直到P为NULL并且栈为空则遍历结束s

'''

'''
Complexity Analysis

Time complexity : O(n).

Space complexity : O(n). 
'''

# Definition for binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right =None

class Solution(object):
	def inorderTraversal(self, root):
		"""
        :type root: TreeNode
        :rtype: List[int]
        """
        # 使用一个栈来存储二叉树节点
		stack = []
		res = []
		node = root  # node一开始存放的是根节点root的地址
		

		while True:
			while node:   #若当前节点存在时（node, node.left, node.right等以此类推）
				stack.append(node)  
				# print("stack压入的值 = ",node.val)
				node = node.left   # 如果左子节点不为空，则继续将左子节点入栈,直到左子节点为None时退出循环
			if stack == []:  #如果栈最终为空，则循环结束
				break  #break跳出的是最近的一个循环
			else:
				# 如果左子节点为空，则抛出栈顶节点并记录 val 值，然后将其右子节点入栈
				node = stack.pop()
				# print("栈pop出去的值 = ",node.val)
				res.append(node.val)
				node = node.right  # 将其右子节点入栈, 直到右子节点为None时退出循环

		#print(res)
		return res


if __name__ == '__main__':
    
    s= Solution()

    r = TreeNode(28)
    r.left = TreeNode(16)
    r.right = TreeNode(30)
    
    r.left.left = TreeNode(13)
    r.left.right = TreeNode(22)
    
    r.right.left = TreeNode(29)
    r.right.right = TreeNode(42)
    result = s.inorderTraversal(r)
    print(result)


'''
思考：
题中说明了要求使用迭代法

迭代
先一股脑把左边一条线全部push到底（即走到最左边），然后node最终为None了就开始pop stack了，
然后因为pop出来的每一个node都是自己这棵树的root，所以看看它有没有右孩子，
没有那肯定继续pop，有的话自然而然右孩子是下一个要被访问的节点。

使用一个栈来存储二叉树节点，根据中序遍历的规则，我们可以推算出这样的规律： 
1. 将当前非空节点入栈 
2. 如果左子节点不为空，则继续将左子节点入栈 
3. 如果左子节点为空，则抛出栈顶节点并记录 val 值，然后将其右子节点入栈 
4. 重复 1、2、3 步骤直至栈空
'''

