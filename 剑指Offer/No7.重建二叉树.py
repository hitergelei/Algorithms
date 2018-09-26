'''
链接：https://www.nowcoder.com/questionTerminal/8a19cbe657394eeaac2f6ea9b0f6fcf6
来源：牛客网

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


#方法三好理解
class Solution:
    def reConstructBinaryTree(self, pre, tin):
    	#为什么if not pre or not tin:return None可以通过，
    	#但是写成if pre == None or tin == None:return None就报错
    	#答：pre和tin是list，not [] 是True，== []也是True。你改成==[]试试
        if not pre or not tin:   #if pre == [] or tin == []:
            return None
        root = TreeNode(pre[0])
        #print("root.val= ", root.val)
        index = tin.index(root.val)
        #print("index = ", index)
        root.left = self.reConstructBinaryTree(pre[1:index+1], tin[:index]) 
        root.right = self.reConstructBinaryTree(pre[index+1:], tin[index + 1:])
       
        return root

pre = [1,2,4,7,3,5,6,8]

tin = [4,7,2,1,5,3,8,6]
test = Solution()
print(test.reConstructBinaryTree(pre, tin).val)



# class Solution:
#     # 返回构造的TreeNode根节点
#     def reConstructBinaryTree(self, pre, tin):
#         # write code here
#         if not pre or not tin:
#             return None
#         root=TreeNode(pre[0])
#         val=tin.index(pre[0])
        
#         root.left=self.reConstructBinaryTree(pre[1:val+1],tin[:val])
#         root.right=self.reConstructBinaryTree(pre[val+1:],tin[val+1:])
#         return root



#方法二
# class Solution:
#     def reConstructBinaryTree(self, pre, tin):
#     	#为什么if not pre or not tin:return None可以通过，
#     	#但是写成if pre == None or tin == None:return None就报错
#     	#答：pre和tin是list，not [] 是True，== []也是True。你改成==[]试试
#         if not pre or not tin:   #if pre == [] or tin == []:
#             return None
#         root = TreeNode(pre.pop(0))
#         index = tin.index(root.val)
#         #每颗子树的根节点肯定是pre子数组的首元素，所以每次新建一个子树的根节点
#         root.left = self.reConstructBinaryTree(pre, tin[:index])
#         root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
#         return root

#重建时先建立左子树时，会将pre中的内容一个个pop掉，这样到建立右子树时，pre中已经不包含左子树中的内容了。
#能否解释一下为什么root = TreeNode(pre.pop(0))可以，但是用root = TreeNode(pre[0])就不行了呢?
#答：root = TreeNode(pre[0])没把元素删掉，重建右子树的时候pre中还会有左子树的元素





# class Solution:
# 	#返回构造的TreeNode根节点
# 	def reConstructBinaryTree(self, pre,tin):
# 		#write code here
# 		if not pre and not tin:
# 			return None
# 		root = TreeNode(pre[0])
# 		#print(root,root.val)
# 		if set(pre) != set(tin):
# 			return None
# 		i = tin.index(pre[0])
# 		print('i = ',i )
# 		root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
# 		root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
# 		return root


# pre = [1,2,4,7,3,5,6,8]
# tin = [4,7,2,1,5,3,8,6]
# test = Solution()
# #print(test.reConstructBinaryTree(pre, tin).val)
# newTree = test.reConstructBinaryTree(pre,tin)
# #按层序遍历输出树中某一层的值
# def PrintNodeAtLevel(TreeNode, level):
# 	if not TreeNode or level <0:
# 		return 0
# 	if level == 0:
# 		print(TreeNode.val)
# 		return 1
# 	PrintNodeAtLevel(TreeNode.left, level-1)
# 	PrintNodeAtLevel(TreeNode.right, level-1)

# # 已知树的深度按层遍历输出树的值
# def PrintNodeByLevel(treeNode, depth):
#     for level in range(depth):
#         PrintNodeAtLevel(treeNode, level)

# PrintNodeByLevel(newTree, 5)


