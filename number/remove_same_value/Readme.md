# 27. Remove Element

**Difficulty:** Easy

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**. The order of the remaining elements may be changed.

Return the number of elements in `nums` that are **not equal** to `val`.

The array should be modified such that the first `k` elements contain all the elements that are not equal to `val`, where `k` is the returned value. The remaining elements beyond the first `k` positions are not important.

---

## Custom Judge

The judge will test your solution using code similar to the following:

```java
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // Expected array (sorted, without val)

int k = removeElement(nums, val);

assert k == expectedNums.length;
sort(nums, 0, k);

for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, your solution will be accepted.

---

## Example 1

### Input

```text
nums = [3,2,2,3], val = 3
```

### Output

```text
2
```

### Explanation

The first two elements of `nums` should be `2` and `2`.

One possible modified array is:

```text
[2,2,_,_]
```

The remaining elements are ignored.

---

## Example 2

### Input

```text
nums = [0,1,2,2,3,0,4,2], val = 2
```

### Output

```text
5
```

### Explanation

One possible modified array is:

```text
[0,1,4,0,3,_,_,_]
```

The first five elements can be in any order as long as they do not contain `2`.

---

## Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`