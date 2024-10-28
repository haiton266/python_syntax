Below are detailed explanations of **Sliding Window**, **Prefix Sum**, and **Hashing** techniques, which you can use for your interview preparation:

---

## **1. Sliding Window Technique**

### **What is it?**

The **Sliding Window** technique is used to solve problems involving subarrays or substrings. A "window" represents a subset of the data structure (usually contiguous) that can move forward over the data. This technique is especially useful for problems requiring the analysis of a specific segment (like a subarray of length `k`) of the data structure without recalculating the entire segment every time.

### **Key Idea**

- Instead of recalculating the sum/product/other properties of a subarray or substring from scratch, maintain a window that slides over the data and updates the required properties incrementally.
- This often reduces the time complexity from O(n^2) to O(n).

### **Types of Sliding Windows**

- **Fixed Size**: The window size remains constant.
- **Dynamic Size**: The window size can grow or shrink depending on the problem's constraints.

### **Common Use Cases**

- Finding the maximum or minimum sum of a subarray of size `k`.
- Longest substring with no repeating characters.
- Longest subarray with a given sum.

### **Example Problem: Maximum Sum Subarray of Size `k`**

**Problem**: Given an array of integers and an integer `k`, find the maximum sum of any contiguous subarray of size `k`.

**Solution**:

```python
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return None

    # Calculate the sum of the first window
    max_sum = current_sum = sum(arr[:k])

    # Slide the window from start to end
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))  # Output: 9
```

### **Advantages**

- Converts O(n^2) problems to O(n) in many cases.
- Easy to implement for fixed-size windows.

### **Disadvantages**

- Works only for problems that involve contiguous subarrays or substrings.

---

## **2. Prefix Sum Technique**

### **What is it?**

The **Prefix Sum** technique involves precomputing cumulative sums of an array, which allows for quick range queries. This technique helps avoid recalculating the sum from scratch every time, especially when dealing with repetitive range sum queries.

### **Key Idea**

- Create a prefix sum array, where each element at index `i` stores the sum of the array elements from the start to `i`.
- This allows you to calculate the sum of any subarray `[i, j]` in constant time using the formula:
  \[
  \text{Sum}[i, j] = \text{prefix_sum}[j] - \text{prefix_sum}[i-1]
  \]

### **Common Use Cases**

- Range sum queries.
- Finding subarrays with a specific sum.
- Problems involving cumulative sums or counts.

### **Example Problem: Range Sum Query**

**Problem**: Given an array of integers, answer multiple queries asking for the sum of elements between indices `i` and `j`.

**Solution**:

```python
def create_prefix_sum(arr):
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]

    # Precompute prefix sums
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    return prefix_sum

def range_sum(prefix_sum, i, j):
    if i == 0:
        return prefix_sum[j]
    return prefix_sum[j] - prefix_sum[i - 1]

# Example usage:
arr = [2, 4, 5, 7, 8, 9]
prefix_sum = create_prefix_sum(arr)
print(range_sum(prefix_sum, 1, 3))  # Output: 16 (4 + 5 + 7)
```

### **Advantages**

- Reduces time complexity for multiple range sum queries from O(n) to O(1) per query after O(n) preprocessing.
- Useful for 1D and 2D problems.

### **Disadvantages**

- Requires extra memory for the prefix sum array.
- Does not work well with problems involving non-contiguous subarrays.

---

## **3. Hashing Technique**

### **What is it?**

**Hashing** involves using a hash table (or dictionary in Python) to achieve constant-time complexity for lookups, insertions, and deletions. Hashing maps data (keys) to values using a hash function, allowing for efficient access to elements.

### **Key Idea**

- Use a hash table (like a Python `dict` or `set`) to store elements or counts of elements.
- Provides O(1) average time complexity for insert, delete, and search operations.
- Often used to check for existence, count frequencies, or find duplicates.

### **Common Use Cases**

- Finding pairs in an array with a specific sum.
- Checking for duplicates in a data set.
- Frequency counting.
- Implementing caches (e.g., LRU Cache).

### **Example Problem: Two Sum**

**Problem**: Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to the target. Assume there is exactly one solution.

**Solution**:

```python
def two_sum(nums, target):
    num_map = {}  # Value to index mapping

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
```

### **Advantages**

- Efficient lookups, insertions, and deletions.
- Great for problems involving frequency counting and existence checks.

### **Disadvantages**

- Hash collisions can degrade performance in worst-case scenarios.
- Uses extra memory for the hash table.
- Hashing only works with hashable data types (like integers, strings).

---

### **Summary**

| **Technique**  | **Use Cases**                               | **Time Complexity**            | **Key Idea**                                        |
| -------------- | ------------------------------------------- | ------------------------------ | --------------------------------------------------- |
| Sliding Window | Subarrays, substrings                       | O(n)                           | Slide a window over data, update incrementally.     |
| Prefix Sum     | Range sum queries, cumulative counts        | O(n) preprocessing, O(1) query | Precompute cumulative sums for quick range queries. |
| Hashing        | Frequency counting, existence checks, pairs | O(1) average for lookups       | Use a hash table for constant-time operations.      |

These three techniques are essential for solving a variety of problems in competitive programming and technical interviews. They provide powerful tools to optimize solutions from higher complexities to linear or near-linear complexities.
