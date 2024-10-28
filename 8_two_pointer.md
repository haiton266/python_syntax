### **Two-Pointer Problems**

#### 1. **Two Sum (Sorted Array)**

- **Problem**: Given a sorted array of integers and a target sum, find two numbers such that their sum is equal to the target. Return their indices (1-based index).
- **Input**: `numbers = [2, 7, 11, 15]`, `target = 9`
- **Output**: `[1, 2]` (because `numbers[0] + numbers[1] == 9`)
- **Approach**: Use two pointers. Start with one pointer at the beginning (`left`) and the other at the end (`right`) of the array. If the sum is less than the target, move the left pointer to the right. If the sum is greater, move the right pointer to the left.

```python
def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # Return 1-based indices
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []  # No solution
```

#### 2. **Container with Most Water**

- **Problem**: Given an array of non-negative integers where each element represents the height of a vertical line, find two lines that together with the x-axis form a container, such that it holds the most water.
- **Input**: `height = [1,8,6,2,5,4,8,3,7]`
- **Output**: `49` (Max area between index 1 and index 8)
- **Approach**: Use two pointers, one at the start and one at the end. Calculate the area formed by the lines at the two pointers, then move the shorter line’s pointer inward.

```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        max_water = max(max_water, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water
```

#### 3. **3Sum**

- **Problem**: Given an array `nums` of integers, find all unique triplets `(a, b, c)` such that `a + b + c = 0`.
- **Input**: `nums = [-1, 0, 1, 2, -1, -4]`
- **Output**: `[[-1, -1, 2], [-1, 0, 1]]`
- **Approach**: Sort the array. Iterate with a fixed pointer and use two pointers for the remaining two values to find the triplets.

```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return result
```
