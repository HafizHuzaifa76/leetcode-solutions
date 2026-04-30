# 3Sum Closest

## Problem Statement

Given an integer array `nums` and an integer `target`, find a triplet in `nums` such that the sum is closest to `target`.

Return the sum of the triplet.

You may assume that each input would have exactly one solution.

---

## Example 1

### Input

nums = [-1, 2, 1, -4]
target = 1


### Output

2


### Explanation
The sum that is closest to the target is:
- (-1 + 2 + 1) = 2

---

## Example 2

### Input

nums = [0, 0, 0]
target = 1


### Output

0


### Explanation
All possible triplets sum to 0, which is the closest to 1.

---

## Constraints

- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10^4 <= target <= 10^4`

---

## Follow-up

Can you solve it in better than O(n³) time complexity?