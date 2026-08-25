class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        best = []
        count = [0]*26
        for right in range (len(s)):
            ch = s[right]
            length = right - left + 1
            count[ord(ch) - ord('A')] += 1
            max_freq = max(max_freq, count[ord(ch) - ord('A')])
            
            if length - max_freq <= k:
                best.append(length)
                
            else:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
        return max(best)
