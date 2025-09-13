class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        longest_str = 0
        current_str = 0
        last_idx = 0

        for c in s:
            if not freq.get(c, None):
                freq[c] = 1
                current_str += 1
                longest_str = max(longest_str, current_str)
                continue
            freq[c] += 1
            current_str += 1
            while freq[c] != 1:
                freq[s[last_idx]] -= 1
                last_idx += 1
                current_str -= 1
        return longest_str

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))