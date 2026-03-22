# 11. Container With Most Water

**Medium** | **Topics**: Array, Two Pointers, Greedy | **Companies**: Amazon, Google, Microsoft, Facebook, Bloomberg, Uber, Apple, Adobe, Oracle

---

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the **maximum amount of water** a container can store.

**Notice** that you may not slant the container.

---

## Examples

### Example 1
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.


**Visualization:**
Index: 0 1 2 3 4 5 6 7 8
Height: 1 8 6 2 5 4 8 3 7

The best container uses lines at index 1 (height 8) and index 8 (height 7):

Width = 8 - 1 = 7
Height = min(8, 7) = 7
Area = 7 × 7 = 49


### Example 2
Input: height = [1,1]
Output: 1
Explanation: Width = 1, Height = min(1,1) = 1, Area = 1 × 1 = 1


### Example 3
Input: height = [1,3,2,5,25,24,5]
Output: 24? Let's calculate:

Best container is between index 4 (25) and index 5 (24)

Width = 1, Height = min(25,24) = 24, Area = 24

---

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

## Formula

The area between two lines at indices `i` and `j` (where `i < j`) is:
Area = (j - i) × min(height[i], height[j])

