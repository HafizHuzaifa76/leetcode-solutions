class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            str = f'{x}'
            if str == str[::-1]:
                return True
            else:
                return False