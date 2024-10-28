# Python Guide for Interview: Data Structures and Algorithms

📌 This repository is a collection of Python solutions and notes aimed at preparing for technical interviews, specifically focusing on Data Structures and Algorithms.

📌 This is my Leetcode nickname: https://leetcode.com/u/haikesuki/

Useful link i will read: https://wiki.vnoi.info/algo/data-structures/data-structures-overview

## Some technique helps code more efficiently

### 1. **`enumerate()`**

- **What it does**: Instead of using a `for` loop with a manual index counter, `enumerate()` allows you to loop over an iterable (like a list) and have an automatic index.
- **Syntax**: `for index, value in enumerate(iterable)`
- **Benefit**: Makes the code shorter, cleaner, and avoids potential off-by-one errors.

**Example**:

```python
# Without enumerate:
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(i, fruits[i])

# With enumerate:
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

### 2. **`zip()`**

- **What it does**: Takes multiple iterables (like lists) and returns an iterator that aggregates elements from each iterable into tuples.
- **Syntax**: `for item1, item2 in zip(iterable1, iterable2)`
- **Benefit**: Combines multiple lists (or other iterables) easily without requiring you to manage indices.

**Example**:

```python
# Without zip:
names = ['John', 'Jane', 'Doe']
ages = [23, 29, 34]
for i in range(len(names)):
    print(names[i], ages[i])

# With zip:
for name, age in zip(names, ages):
    print(name, age)
```

### 3. **List Comprehensions**

- **What it does**: A concise way to create lists using a single line of code.
- **Syntax**: `[expression for item in iterable if condition]`
- **Benefit**: Faster and more readable than using a `for` loop to populate a list.

**Example**:

```python
# Without list comprehension:
squares = []
for i in range(10):
    squares.append(i * i)

# With list comprehension:
squares = [i * i for i in range(10)]
```

### 4. **Dictionary Comprehensions**

- **What it does**: Similar to list comprehensions, but used to create dictionaries.
- **Syntax**: `{key_expression: value_expression for item in iterable if condition}`
- **Benefit**: More concise and expressive for creating dictionaries.

**Example**:

```python
# Without dictionary comprehension:
names = ['apple', 'banana', 'cherry']
lengths = {}
for name in names:
    lengths[name] = len(name)

# With dictionary comprehension:
lengths = {name: len(name) for name in names}
```

### 5. **`any()` and `all()`**

- **What they do**: `any()` checks if any element in an iterable is `True`. `all()` checks if all elements are `True`.
- **Benefit**: Simple way to perform logical checks on an iterable.

**Example**:

```python
# Without any():
values = [0, None, False, 5]
found = False
for val in values:
    if val:
        found = True
        break

# With any():
found = any(values)

# With all():
all_positive = all(x > 0 for x in [1, 2, 3, 4])  # Returns True if all are positive
```

### 6. **`set()` for Unique Elements**

- **What it does**: A `set` is an unordered collection of unique elements.
- **Benefit**: Removes duplicates efficiently or checks membership faster than lists.

**Example**:

```python
# Without set:
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# With set:
unique_numbers = list(set(numbers))
```

### 7. **`collections.defaultdict`**

- **What it does**: A dictionary that provides a default value for a key that does not exist.
- **Benefit**: Simplifies counting, grouping, or initializing nested dictionaries.

**Example**:

```python
from collections import defaultdict

# Without defaultdict:
counts = {}
words = ['apple', 'banana', 'apple']
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

# With defaultdict:
counts = defaultdict(int)
for word in words:
    counts[word] += 1
```

### 8. **`with` Statement for File Handling**

- **What it does**: Manages file opening and closing automatically using a context manager.
- **Benefit**: Prevents file-handling bugs and makes the code cleaner.

**Example**:

```python
# Without with:
file = open('example.txt', 'r')
data = file.read()
file.close()

# With with:
with open('example.txt', 'r') as file:
    data = file.read()
```

### 9. **`sorted()` with Custom Key**

- **What it does**: Sorts an iterable with an optional custom sorting logic.
- **Syntax**: `sorted(iterable, key=function)`
- **Benefit**: Cleaner and more efficient than manually sorting data.

**Example**:

```python
# Sorting a list of tuples by the second element:
data = [('apple', 2), ('banana', 3), ('cherry', 1)]

# Without custom key:
data.sort(key=lambda x: x[1])

# With sorted():
sorted_data = sorted(data, key=lambda x: x[1])
```

### Some examples

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
