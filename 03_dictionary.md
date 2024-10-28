Here's a concise guide for using dictionaries in Python, specifically geared towards coding competitions like Codeforces:

### 1. **Creating a Dictionary**

- **Empty dictionary**:

  ```python
  my_dict = {}
  ```

- **Dictionary with initial key-value pairs**:

  ```python
  my_dict = {"name": "Alice", "age": 25}
  ```

### 2. **Accessing and Modifying Elements**

- **Access a value by key**:

  ```python
  name = my_dict["name"]  # Output: "Alice"
  ```

- **Get a value with a default (if the key might not exist)**:

  ```python
  age = my_dict.get("age", 0)  # Returns 25 if "age" exists, otherwise 0
  ```

- **Add or update a key-value pair**:

  ```python
  my_dict["name"] = "Bob"
  my_dict["city"] = "New York"
  ```

- **Delete a key-value pair**:

  ```python
  del my_dict["age"]
  ```

### 3. **Dictionary Iteration**

- **Iterate over keys**:

  ```python
  for key in my_dict:
      print(key, my_dict[key])
  ```

- **Iterate over values**:

  ```python
  for value in my_dict.values():
      print(value)
  ```

- **Iterate over key-value pairs**:

  ```python
  for key, value in my_dict.items():
      print(key, value)
  ```

### 4. **Checking Existence of a Key**

- **Check if a key exists**:

  ```python
  if "name" in my_dict:
      print("Name is present")
  ```

### 5. **Dictionary Functions**

- **Get all keys**:

  ```python
  keys = list(my_dict.keys())  # Returns a list of all keys
  ```

- **Get all values**:

  ```python
  values = list(my_dict.values())  # Returns a list of all values
  ```

- **Get all key-value pairs**:

  ```python
  items = list(my_dict.items())  # Returns a list of (key, value) tuples
  ```

- **Length of a dictionary**:

  ```python
  length = len(my_dict)  # Number of key-value pairs
  ```

### 6. **Dictionary Methods**

- **Remove a key and return its value**:

  ```python
  value = my_dict.pop("name", None)  # Returns the value or None if the key doesn't exist
  ```

- **Clear all items from the dictionary**:

  ```python
  my_dict.clear()
  ```

- **Merge two dictionaries** (Python 3.9+):

  ```python
  dict1 = {"a": 1, "b": 2}
  dict2 = {"b": 3, "c": 4}
  merged = dict1 | dict2  # Result: {'a': 1, 'b': 3, 'c': 4}
  ```

- **Update a dictionary with another dictionary**:

  ```python
  my_dict.update({"age": 30, "country": "USA"})
  ```

### 7. **Dictionary Comprehensions**

- **Create a dictionary from a list**:

  ```python
  squares = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
  ```

### 8. **Counting Elements with `collections.Counter`**

- **Using `Counter` to count occurrences**:

  ```python
  from collections import Counter
  numbers = [1, 2, 2, 3, 3, 3]
  count = Counter(numbers)  # Result: {3: 3, 2: 2, 1: 1}
  ```

### 9. **Sorting a Dictionary**

- **Sort dictionary by keys**:

  ```python
  sorted_by_keys = dict(sorted(my_dict.items()))  # Sorts by key
  ```

- **Sort dictionary by values**:

  ```python
  sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))  # Sorts by value
  ```

## In practice

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
