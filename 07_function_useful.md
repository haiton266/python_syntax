### 1. **Sorting**

- **Sort a list (ascending order)**:

  ```python
  arr = [5, 2, 9, 1, 5, 6]
  arr.sort()  # In-place sort: [1, 2, 5, 5, 6, 9]
  ```

- **Sort a list in descending order**:

  ```python
  arr.sort(reverse=True)  # [9, 6, 5, 5, 2, 1]
  ```

- **Sort and save order list**:

  ```python
  # Original list
  original_list = [5, 3, 8, 1, 4]

  # Create a list of tuples (index, value)

  indexed_list = list(enumerate(original_list))

  # Sort the list by the value

  sorted_list = sorted(indexed_list, key=lambda x: x[1])

  # Print the sorted list with original indices

  print("Sorted with original indices:", sorted_list)
  ```

- **Sort without modifying the original list**:

  ```python
  sorted_arr = sorted(arr)  # Returns a sorted copy
  ```

````

- **Sort a list of tuples by a specific key**:

  ```python
  data = [(1, 'b'), (2, 'a'), (3, 'c')]
  sorted_data = sorted(data, key=lambda x: x[1])  # Sorts by second element
  ```

### 2. **Mathematical Operations**

- **Find the minimum/maximum element**:

  ```python
  min_val = min(arr)  # 1
  max_val = max(arr)  # 9
  ```

- **Calculate the sum of elements in a list**:

  ```python
  total = sum(arr)  # 28
  ```

- **Absolute value**:

  ```python
  abs_val = abs(-10)  # 10
  ```

### 3. **Searching**

- **Linear search** (finding an element's index):

  ```python
  def linear_search(arr, target):
      for i in range(len(arr)):
          if arr[i] == target:
              return i
      return -1  # Return -1 if not found

  index = linear_search(arr, 5)  # Finds the first occurrence of 5
  ```

### 4. **Combinations and Permutations**

- **Generate combinations**:

  ```python
  def generate_combinations(arr, r):
      if r == 0:
          yield []
      elif len(arr) < r:
          return
      else:
          for i in range(len(arr)):
              for tail in generate_combinations(arr[i+1:], r-1):
                  yield [arr[i]] + tail

  combinations = list(generate_combinations([1, 2, 3], 2))  # [[1, 2], [1, 3], [2, 3]]
  ```

- **Generate permutations**:

  ```python
  def generate_permutations(arr):
      if len(arr) == 0:
          yield []
      else:
          for i in range(len(arr)):
              rest = arr[:i] + arr[i+1:]
              for perm in generate_permutations(rest):
                  yield [arr[i]] + perm

  permutations = list(generate_permutations([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], ...]
  ```

### 5. **String Operations**

- **Sort characters in a string**:

  ```python
  s = "dcba"
  sorted_s = ''.join(sorted(s))  # 'abcd'
  ```

- **Count characters in a string**:

  ```python
  def count_characters(s):
      count = {}
      for char in s:
          count[char] = count.get(char, 0) + 1
      return count

  char_count = count_characters("aabbcc")  # {'a': 2, 'b': 2, 'c': 2}
  ```

### 6. **Greatest Common Divisor (GCD) and Least Common Multiple (LCM)**

- **Find the GCD**:

  ```python
  def gcd(x, y):
      while y != 0:
          x, y = y, x % y
      return x

  gcd_val = gcd(8, 12)  # 4
  ```

- **Calculate the LCM**:

  ```python
  def lcm(x, y):
      return (x * y) // gcd(x, y)

  lcm_val = lcm(8, 12)  # 24
  ```

### 7. **Matrix Operations**

- **Transpose a matrix**:

  ```python
  matrix = [[1, 2, 3], [4, 5, 6]]
  transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
  ```

- **Create a matrix filled with zeros**:

  ```python
  rows, cols = 3, 4
  matrix = [[0] * cols for _ in range(rows)]
  ```

### 8. **Finding Prime Numbers (Sieve of Eratosthenes)**

- **Generate a list of prime numbers up to `n`**:

  ```python
  def sieve_of_eratosthenes(n):
      primes = [True] * (n + 1)
      primes[0] = primes[1] = False
      for i in range(2, int(n**0.5) + 1):
          if primes[i]:
              for j in range(i*i, n + 1, i):
                  primes[j] = False
      return [i for i in range(n + 1) if primes[i]]

  primes_up_to_50 = sieve_of_eratosthenes(50)
  ```

### 9. **Binary Search**

- **Binary search in a sorted list**:

  ```python
  def binary_search(arr, target):
      left, right = 0, len(arr) - 1
      while left <= right:
          mid = (left + right) // 2
          if arr[mid] == target:
              return mid
          elif arr[mid] < target:
              left = mid + 1
          else:
              right = mid - 1
      return -1  # Return -1 if not found

  sorted_arr = [1, 2, 3, 4, 5, 6]
  index = binary_search(sorted_arr, 4)  # 3
  ```

### 10. **Handling Large Numbers (Modular Arithmetic)**

- **Modular exponentiation**:

  ```python
  def mod_exp(base, exp, mod):
      result = 1
      while exp > 0:
          if exp % 2 == 1:
              result = (result * base) % mod
          base = (base * base) % mod
          exp //= 2
      return result

  result = mod_exp(2, 10, 1000)  # 2^10 % 1000 = 24
  ```

### 11. **Finding Subsets**

- **Generate all subsets of a list**:

  ```python
  def generate_subsets(arr):
      result = [[]]
      for num in arr:
          result += [item + [num] for item in result]
      return result

  subsets = generate_subsets([1, 2, 3])  # [[], [1], [2], [1, 2], [3], [1, 3], ...]
  ```
````
