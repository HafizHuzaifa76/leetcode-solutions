## Roman to Integer

### Problem Statement

Given a string `s` representing a Roman numeral, convert it to an integer.

Roman numerals are represented by seven symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

---

### Special Rules (Subtractive Notation)

In some cases, a smaller numeral placed before a larger one indicates subtraction:

- `IV` = 4 (5 - 1)
- `IX` = 9 (10 - 1)
- `XL` = 40 (50 - 10)
- `XC` = 90 (100 - 10)
- `CD` = 400 (500 - 100)
- `CM` = 900 (1000 - 100)

---

### Task

Convert the given Roman numeral string `s` into its integer equivalent.

---

### Example 1

**Input:**

s = "III"


**Output:**

3


---

### Example 2

**Input:**

s = "IV"


**Output:**

4


---

### Example 3

**Input:**

s = "MCMXCIV"


**Output:**

1994


---

### Constraints

- `1 <= s.length <= 15`
- `s` contains only the characters: `I, V, X, L, C, D, M`
- Input is guaranteed to be a valid Roman numeral in the range `[1, 3999]`

---

### Follow-up

Can you solve this in **O(n)** time using a single pass without explicitly checking all subtractive pairs