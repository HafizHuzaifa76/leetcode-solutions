## Valid Parentheses

### Problem Statement

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

A string is considered valid if:

- Every opening bracket has a corresponding closing bracket of the same type.
- Brackets are closed in the correct order.
- Every closing bracket has a matching opening bracket.

### Examples

#### Example 1
**Input:**

s = "()"

**Output:**
true

---

#### Example 2
**Input:**

s = "()[]{}"

**Output:**
true

---

#### Example 3
**Input:**

s = "(]"

**Output:**
false

---

#### Example 4
**Input:**

s = "([)]"

**Output:**
false

---

#### Example 5
**Input:**

s = "{[]}"

**Output:**
true

### Constraints

- `1 <= s.length <= 10^4`
- `s` consists only of parentheses characters: `()[]{}`

### Follow-up

Can you solve it using a stack in O(n) time complexity and O(n) space complexity?