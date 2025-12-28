class Solution:
    def reverse(self, x: int) -> int:
        rev = ''
        is_negative = False

        if x < 0:
            x = x * -1
            is_negative = True

        while x >= 10:
            rem = x % 10
            x = x // 10

            rev = f'{rev}{rem}'

        if is_negative:
            rev = f'-{rev}{x}'
        else:
            rev = f'{rev}{x}'

        num = int(rev)
        
        if num < -2**31 or num > 2**31 - 1:
            return 0

        return num