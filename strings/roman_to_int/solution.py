class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        pairs = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        starters = ['I','X','C']

        num = 0
        skip = False

        for i in range(len(s)):
            if skip:
                skip = False
                continue
            
            char = s[i]
            if char in starters and i < len(s)-1:
                chars = char + s[i+1]
                if chars in pairs:
                    num += pairs[chars]
                    skip = True
                else:
                    num += romans[char]
            else:
                num += romans[char]

        return num