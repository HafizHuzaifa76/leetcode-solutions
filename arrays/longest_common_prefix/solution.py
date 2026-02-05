from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        lt = ""
        length = len(strs[0])
        i = 0

        while i < length:
            
            for index, str in enumerate(strs):
                if index == 0:
                    lt = lt + str[i]

                prefix = lt  

                if not str.startswith(lt):
                    prefix = lt[:-1]
                    i = length + 1
                    break

            i += 1

        return prefix


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    ex1 = sol.longestCommonPrefix(["flower", "flow", "flight"]) # "fl"
    print(f'Expected : "fl", Result: {ex1}')  

    # Example 2
    ex2 = sol.longestCommonPrefix(["dog", "racecar", "car"])  # ""
    print(f'Expected : "", Result: {ex2}')  