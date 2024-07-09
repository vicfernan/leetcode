class Solution(object):
    def substrin(self, s, c):
        i = 0
        while (i < len(s)):
            if (s[i] == c):
                return i
            i += 1

        return -1


    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        st1 = ''
        st2 = ''
        while i < len(s):
            if (self.substrin(st1, s[i]) == -1):
                st1 += s[i]
            else:
                if (len(st1) > len(st2) or st2 == ''):
                    st2 = st1
                i -= len(st1)
                st1 = ''
            i += 1
        if (len(st1) > len(st2)):
            return len(st1)
        return len(st2)