# 6. Zigzag Conversion

## Problem Statement

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows, then read line by line.

### Example (numRows = 3)

P A H N
A P L S I I G
Y I R


Reading line by line produces:

PAHNAPLSIIGYIR


### Task

Write a function:

string convert(string s, int numRows);

that converts the input string `s` into its zigzag form based on `numRows`.

---

## Examples

### Example 1
**Input**
s = "PAYPALISHIRING", numRows = 3

**Output**
"PAHNAPLSIIGYIR"

### Example 2
**Input**
s = "PAYPALISHIRING", numRows = 4

**Output**
"PINALSIGYAHRPI"


**Explanation**
P I N
A L S I G
Y A H R
P I


### Example 3
**Input**
s = "A", numRows = 1

**Output**
"A"