class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_end = len(needle)
        hstack_length = len(haystack)
        
        for i in range(hstack_length):
            if haystack[i] == needle[0] and i + needle_end <= hstack_length :
                sub = haystack[i : i+needle_end]
                if sub == needle:
                    return i

        return -1