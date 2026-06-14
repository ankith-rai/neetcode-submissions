class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substr = 1
        char_set = set()
        if len(s) in range(0, 1):
            return len(s)
        l = 0
        
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest_substr = max(longest_substr, (r - l + 1))
        return longest_substr