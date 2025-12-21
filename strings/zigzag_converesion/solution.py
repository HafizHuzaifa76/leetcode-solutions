class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        lst = ["" for _ in range(numRows)]

        row = 0
        add = True

        for char in s:
            lst[row] = lst[row] + char

            if row == numRows-1:
                add = False
            elif row == 0:
                add = True

            if numRows-1 == 0:
                row = 0
            elif add:
                row += 1
            else:
                row -= 1
        
        result = ''
        for i in lst:
            result = result + i

        return result
