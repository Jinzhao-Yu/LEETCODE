#
# @lc app=leetcode.cn id=844 lang=python
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def help(ch):
            slow, fast = 0, 0
            while fast < len(ch):
                if ch[fast] == '#':
                    slow = fast
                fast += 1
            return ch[slow+1:]
        return help(s) == help(t)
# @lc code=end

