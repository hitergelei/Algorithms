'''
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。  
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
#方法一：直接使用Python字符串的内置函数 27ms
class Solution(object):
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if type(s) != str:
        	return 
        return s.replace(' ', '%20')


#方法二：剑指offer原书方法 26ms
    # s 源字符串
    # 判断输入类型的时候，isinstance必须首先判断，
    #因为如果输入为integer的话，没有len，就会直接报错
    def replaceSpace2(self, s):
    	if not isinstance(s, str) or s == None or len(s) <= 0:
    		return ""
    	spaceNum = 0
    	for i in s:
    		if i == " ":
    			spaceNum += 1
        #newstrLen为把空格替换成%20之后的长度
    	newstrLen = len(s) + 2 * spaceNum
    	newStr = newstrLen * [None]

    	p1 = len(s) - 1
    	p2 = newstrLen - 1
    	while p1 >= 0 and p2 >= p1:    		
    		if s[p1] == " ":
    			newStr[p2-2: p2+1] = ['%', '2', '0']
    			p2 -= 3
    			p1 -= 1
    		else:  #字符串逐个复制
    			newStr[p2] = s[p1]
    			p2 -= 1
    			p1 -= 1
    	return "".join(newStr)


#方法三：
# 使用append一次遍历即可替换 25ms
# 由于list的append是O(1)的时间复杂度，除了扩容所导致的时间损耗，该算法复杂度为O(n)
    def replaceSpace3(self, s):
    	string = list(s)
    	stringReplace = []
    	for item in string:
    		if item == " ":
    			stringReplace.append('%')
    			stringReplace.append('2')
    			stringReplace.append('0')
    		else:
    			stringReplace.append(item)

    	return "".join(stringReplace)

s = 'we are happy.'
test = Solution()
print(test.replaceSpace(s))
print(test.replaceSpace2(s))
print(test.replaceSpace3(s))
print(len(s))

# str = "";
# seq = ("a", "b", "c"); # 字符串序列
# print (str.join( seq ));
#输出：abc
