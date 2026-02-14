class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        s1 = strs[0]
        s2 = strs[len(strs) - 1]
        i = 0
        minimum = min(len(s1), len(s2))
        while i < minimum and s1[i] == s2[i]:
            i = i + 1
        return s1[:i]



