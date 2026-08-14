# LeetCode 23 — Merge k Sorted Lists

You are given an array of `k` linked lists, where each linked list is sorted in ascending order.

Merge all the linked lists into **one sorted linked list** and return its head.

## Example

```text
Input:
[
  1 → 4 → 5,
  1 → 3 → 4,
  2 → 6
]

Output:
1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

## Constraints

* `k == lists.length`
* `0 <= k <= 10⁴`
* `0 <= lists[i].length <= 500`
* `-10⁴ <= lists[i][j] <= 10⁴`
* Each `lists[i]` is sorted in ascending order.
* The total number of nodes across all linked lists is at most `10⁴`.

## Goal

Merge all `k` sorted linked lists into a single sorted linked list.
