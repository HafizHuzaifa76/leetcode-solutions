# 12. Integer to Roman

**Difficulty:** Medium

Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|------:|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Roman numerals are usually written from largest to smallest from left to right. However, there are six special cases where subtraction is used:

- `IV` = 4 (`5 - 1`)
- `IX` = 9 (`10 - 1`)
- `XL` = 40 (`50 - 10`)
- `XC` = 90 (`100 - 10`)
- `CD` = 400 (`500 - 100`)
- `CM` = 900 (`1000 - 100`)

## Problem

Given an integer `num`, convert it to its Roman numeral representation.

## Examples

### Example 1

**Input**

```text
num = 3
```

**Output**

```text
"III"
```

**Explanation**

```text
3 = 1 + 1 + 1
```

---

### Example 2

**Input**

```text
num = 58
```

**Output**

```text
"LVIII"
```

**Explanation**

```text
50 = L
5  = V
3  = III

LVIII
```

---

### Example 3

**Input**

```text
num = 1994
```

**Output**

```text
"MCMXCIV"
```

**Explanation**

```text
1000 = M
900  = CM
90   = XC
4    = IV

MCMXCIV
```

## Constraints

```text
1 <= num <= 3999
```

## Key Roman Numerals

| Integer | Roman |
|---------:|:-----|
| 1 | I |
| 4 | IV |
| 5 | V |
| 9 | IX |
| 10 | X |
| 40 | XL |
| 50 | L |
| 90 | XC |
| 100 | C |
| 400 | CD |
| 500 | D |
| 900 | CM |
| 1000 | M |