'''
题目：给定一个字符串，找出不含有重复字符的 最长子串 的长度。

示例： 
给定 “abcabcbb” ，没有重复字符的最长子串是 “abc” ，那么长度就是3。 
给定 “bbbbb” ，最长的子串就是 “b” ，长度是1。 
给定 “pwwkew” ，最长子串是 “wke” ，长度是3。请注意答案必须是一个子串，”pwke” 是 子序列 而不是子串。
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 存储历史循环中最长的子串长度
        max_len = 0
        # 判断传入的字符串是否为空
        if s is None or len(s) == 0:
            return max_len
        # 定义一个字典，存储不重复的字符和字符所在的下标
        str_dict = {}
        # 存储每次循环中最长的子串长度
        one_max = 0
        # 记录最近重复字符所在的位置+1
        start = 0
        for i in range(len(s)):
            # 判断当前字符是否在字典中和当前字符的下标是否大于等于最近重复字符的所在位置
            if s[i] in str_dict and str_dict[s[i]] >= start:
                # 记录当前字符的值+1
                start = str_dict[s[i]] + 1
            #print("start=",start)
            # 在此次循环中，最大的不重复子串的长度
            one_max = i - start + 1
            #print("one_max = ", one_max)
            # 把当前位置覆盖字典中的位置
            str_dict[s[i]] = i
            #print("str_dict[s[%s]] = " %i, str_dict)
            # 比较此次循环的最大不重复子串长度和历史循环最大不重复子串长度
            max_len = max(max_len, one_max)
            #print('max_len = ',max_len)
        return max_len


if __name__ == '__main__':
    sol = Solution()
    # print(sol.lengthOfLongestSubstring("bbbbb"))
    # print(sol.lengthOfLongestSubstring("eeydgwdykpv"))
    print(sol.lengthOfLongestSubstring("pwwkew"))
    # print(sol.lengthOfLongestSubstring("abcabcbb"))


'''
这是一道可以跟Two Sum媲美的题。给了我们一个字符串，让我们求最长的无重复字符的子串，
注意这里是子串，不是子序列，所以必须是连续的。我们先不考虑代码怎么实现，如果给一个例子"abcabcbb"，
让你手动找无重复字符的子串，该怎么找？
一个字符一个字符的遍历，比如a，b，c，然后又出现了一个a，那么此时就应该去掉第一次出现的a，
然后继续往后，又出现了一个b，则应该去掉一次出现的b，以此类推，最终发现最长的长度为3。
所以说，我们需要记录之前出现过的字符，记录的方式有很多，最常见的是统计字符出现的个数，
但是这道题字符出现的位置很重要，所以我们可以使用HashMap来建立字符和其出现位置之间的映射。Python中用字典
'''
# 参考资料 https://www.cnblogs.com/ariel-dreamland/p/8668286.html