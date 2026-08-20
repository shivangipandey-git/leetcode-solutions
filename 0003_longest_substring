class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = set()
        left = 0
        max_count = 0
        for strings in range (len(s)):
            while s[strings] in string:
                string.remove(s[left])
                left+=1
            string.add(s[strings])
            max_count = max(max_count, strings - left + 1)
        return max_count
        