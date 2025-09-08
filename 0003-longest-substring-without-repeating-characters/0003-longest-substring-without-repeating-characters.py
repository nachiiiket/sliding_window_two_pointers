class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        big_count = 0
        check_dup = []
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            if s[j] not in check_dup:
                check_dup.append(s[j])   # append current character
                count += 1
                j += 1
            else:
                check_dup.pop(0)        # remove from left
                count -= 1
                i += 1
            if count > big_count:
                big_count = count
        return big_count
