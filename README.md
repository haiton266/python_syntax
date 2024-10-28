# Python Guide for Interview: Data Structures and Algorithms

📌 This repository is a collection of Python solutions and notes aimed at preparing for technical interviews, specifically focusing on Data Structures and Algorithms.

## Contents

- **Problem Solving**: Solutions to various problems from LeetCode, categorized and added to the relevant files.
- **Python Syntax**: Examples and explanations for Python syntax, divided into sections 1 to 6.
- **Useful Functions**: A compilation of handy functions, detailed in section 7.
- **Optimization Techniques**: Common techniques to achieve time complexity of O(n), with explanations and examples.

```python
# https://leetcode.com/problems/word-pattern/description/?envType=problem-list-v2&envId=hash-table

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
