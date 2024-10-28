# Python Guide for Interview: Data Structures and Algorithms

📌 This repository is a collection of Python solutions and notes aimed at preparing for technical interviews, specifically focusing on Data Structures and Algorithms.

## Contents

- **Problem Solving**: Solutions to various problems from LeetCode, categorized and added to the relevant files.
- **Python Syntax**: Examples and explanations for Python syntax, divided into sections 1 to 6.
- **Useful Functions**: A compilation of handy functions, detailed in section 7.
- **Optimization Techniques**: Common techniques to achieve time complexity of O(n), with explanations and examples.

Dictionary, zip:
https://leetcode.com/problems/word-pattern/description/?envType=problem-list-v2&envId=hash-table

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_s = {}
        s_to_pattern = {}
        s = s.split()

        # Check if lengths of pattern and s are different
        if len(pattern) != len(s):
            return False

        for pat, word in zip(pattern, s):
            if pat not in pattern_to_s and word not in s_to_pattern:
                pattern_to_s[pat] = word
                s_to_pattern[word] = pat
            elif pattern_to_s.get(pat) != word or s_to_pattern.get(word) != pat:
                return False

        return True

# Example usage
print(Solution().wordPattern("abba", "dog cat cat dog"))
```

Sort, save location: https://leetcode.com/problems/largest-number-at-least-twice-of-others/?envType=problem-list-v2&envId=sorting

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        indexed_list = list(enumerate(nums))
        indexed_list = sorted(indexed_list, key=lambda x: x[1])
        n = len(nums)
        if indexed_list[n-1][1] >= indexed_list[n-2][1] * 2:
            return indexed_list[n-1][0]
        else:
            return -1
```

Convert a string to a list of integers, initialize a list full of zeros, iterate with an id list.: https://leetcode.com/problems/maximum-score-after-splitting-a-string/?envType=problem-list-v2&envId=prefix-sum

```python
class Solution:
    def maxScore(self, s: str) -> int:
        nums = [int(char) for char in s] # Convert str to list int
        n = len(nums)
        sum = [0] * n
        for id, num in enumerate(nums):
            if id == 0:
                sum[id] = num
            else:
                sum[id] = sum[id - 1] + num

        result = 0
        for loc in range(0, n-1):
            result = max(result, loc - sum[loc] + 1 + sum[n-1] - sum[loc])
        return result
```
