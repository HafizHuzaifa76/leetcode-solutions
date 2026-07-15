class Solution:
    roman = {
        0: '',
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    
    keys = list(roman.keys())

    def intToRoman(self, num: int) -> str:
        i = 1
        value = ''

        while num > 0 :
            s = num % 10
            n = s * i
            value = self.getRoman(n) + value
            i *= 10
            num //= 10

        return value

    def getRoman(self, num: int) -> str:

        val = self.roman.get(num)

        if val:
            return val
        else:
            for ind in range(len(self.keys)) :
                key = self.keys[ind]
                if num >= key:
                    if key == 1000 or num < self.keys[ind+1]:
                        val = self.roman.get(key) + self.getRoman(num-key)

        return val