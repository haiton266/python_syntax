Basic Binary search for this problem:
https://leetcode.com/problems/sqrtx/?envType=problem-list-v2&envId=binary-search

```python
class Solution:
    def transform(self, x: int) -> int:
        return x * x

    def mySqrt(self, x: int) -> int:
        low, high = 0, 2**16
        if x < self.transform(low):
            return 0
        if x >= self.transform(high):
            return high

        # Binary search to find the largest number whose square is <= x
        while low <= high:
            mid = (low + high) // 2
            transformed_mid = self.transform(mid)

            if x == transformed_mid:
                return mid  # Found exactly x

            if x > transformed_mid:
                low = mid + 1  # Move to the upper half
            else:
                high = mid - 1  # Move to the lower half

        # Return the closest integer part of the square root
        return high
```
