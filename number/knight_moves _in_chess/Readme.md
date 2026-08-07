# Q1. Even Number of Knight Moves

**Difficulty:** Easy

## Problem Statement

You are given two integer arrays `start` and `target`, where each array is of the form `[x, y]` representing a cell on a standard **8 × 8 chessboard**.

Return `true` if a knight can move from `start` to `target` in an **even number of moves**. Otherwise, return `false`.

> **Note:** A valid knight move consists of moving **two squares in one direction** and **one square perpendicular** to it.

---

## Example 1

### Input

```text
start = [1,1], target = [2,2]
```

### Output

```text
true
```

### Explanation

One possible sequence of moves is:

```text
(1,1) → (3,2) → (2,4) → (4,3) → (2,2)
```

The knight reaches the target in **4 moves**, which is even.

Therefore, the answer is **true**.

---

## Example 2

### Input

```text
start = [4,5], target = [6,6]
```

### Output

```text
false
```

### Explanation

It is impossible to reach `target = [6,6]` from `start = [4,5]` in an **even** number of moves.

Therefore, the answer is **false**.

---

## Constraints

- `start.length == target.length == 2`
- `0 <= start[i], target[i] <= 7`
- Both `start` and `target` represent valid cells on an **8 × 8 chessboard**.