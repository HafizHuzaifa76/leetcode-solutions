# Remove Nth Node From End of List

## Problem Statement

Given the head of a singly linked list, remove the `n`th node from the end of the list and return its head.

---

## Example 1

### Input

head = [1, 2, 3, 4, 5], n = 2


### Output

[1, 2, 3, 5]


### Explanation
The 2nd node from the end is `4`, so it is removed.

---

## Example 2

### Input

head = [1], n = 1


### Output

[]


### Explanation
The only node is removed.

---

## Example 3

### Input

head = [1, 2], n = 1


### Output

[1]


---

## Constraints

- The number of nodes in the list is `k`
- `1 <= k <= 10^5`
- `-10^5 <= Node.val <= 10^5`
- `1 <= n <= k`

---

## Follow-up

Can you solve this in a single pass?