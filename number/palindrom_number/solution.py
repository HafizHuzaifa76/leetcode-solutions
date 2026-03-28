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



class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            rev = x % 10
            num = x / 10
            while num > 1 :
                last = int(num % 10)
                rev = rev*10 + last
                num = num/10

            if x == rev:
                return True
            else:
                return False