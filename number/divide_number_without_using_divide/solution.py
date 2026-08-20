
# this solution is not optimized and gives Time Limit Exceed Error on Large Values
class Solution:
    max_range = 2147483647
    min_range = -2147483648

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend > self.max_range or divisor > self.max_range:
            return self.max_range
        if dividend < self.min_range or divisor < self.min_range:
            return self.min_range
        is_negative = False

        if dividend < 0 and divisor < 0:
            is_negative = False
            dividend = abs(dividend)
            divisor = abs(divisor)
        elif dividend < 0 or divisor < 0:
            is_negative = True
            dividend = abs(dividend)
            divisor = abs(divisor)
        else:
            is_negative = False
        
        if divisor == 1:
            return self.validate_result(-dividend) if is_negative else self.validate_result(dividend)
        
        ans = dividend
        count = 0
        while ans >= divisor:
            count += 1
            ans = ans - divisor

            # if count > 10:
            #     break
        
        return -count if is_negative else count

    def validate_result(self, result: int):
        if result >= self.max_range:
            return self.max_range
        if result < self.min_range:
            return self.min_range
        
        return result