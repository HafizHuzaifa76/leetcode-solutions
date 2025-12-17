class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = []
        max_length = 0

        for char in s:
            if char in unique_chars:
                index = unique_chars.index(char)
                unique_chars = unique_chars[index+1:]
            
            unique_chars.append(char)
            max_length = max(max_length, len(unique_chars))
        
        return max_length