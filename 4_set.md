### 1. **Creating a Set**

- **Empty set**:

  ```python
  my_set = set()
  ```

- **Set with initial elements**:

  ```python
  my_set = {1, 2, 3, 4, 5}
  ```

### 2. **Adding and Removing Elements**

- **Add an element**:

  ```python
  my_set.add(6)  # Adds 6 to the set
  ```

- **Remove an element**:

  ```python
  my_set.remove(3)  # Removes 3 from the set, raises KeyError if 3 is not found
  my_set.discard(3)  # Removes 3, does nothing if 3 is not found
  ```

- **Remove a random element**:

  ```python
  my_set.pop()  # Removes and returns an arbitrary element
  ```

- **Clear the set**:

  ```python
  my_set.clear()  # Removes all elements
  ```

### 3. **Set Operations**

- **Union of two sets**:

  ```python
  set1 = {1, 2, 3}
  set2 = {3, 4, 5}
  union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}
  ```

- **Intersection of two sets**:

  ```python
  intersection_set = set1 & set2  # Output: {3}
  ```

- **Difference of two sets**:

  ```python
  difference_set = set1 - set2  # Output: {1, 2}
  ```

- **Symmetric difference of two sets** (elements in either set1 or set2, but not both):

  ```python
  symmetric_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5}
  ```

### 4. **Checking Membership**

- **Check if an element is in a set**:

  ```python
  if 2 in my_set:
      print("2 is in the set")
  ```

- **Check if an element is not in a set**:

  ```python
  if 10 not in my_set:
      print("10 is not in the set")
  ```

### 5. **Set Methods**

- **`add`**:

  ```python
  my_set.add(7)  # Adds 7 to the set
  ```

- **`update`** (add multiple elements):

  ```python
  my_set.update([8, 9, 10])  # Adds 8, 9, 10 to the set
  ```

- **`union`** (another way to perform union):

  ```python
  union_set = my_set.union({11, 12})
  ```

- **`intersection`** (another way to perform intersection):

  ```python
  intersection_set = my_set.intersection({4, 5, 6})
  ```

- **`difference`** (another way to perform difference):

  ```python
  difference_set = my_set.difference({4, 5, 6})
  ```

- **`symmetric_difference`** (another way to perform symmetric difference):

  ```python
  symmetric_diff_set = my_set.symmetric_difference({5, 6, 7})
  ```

### 6. **Set Comparisons**

- **Subset**:

  ```python
  set1 = {1, 2}
  set2 = {1, 2, 3, 4}
  is_subset = set1.issubset(set2)  # True
  ```

- **Superset**:

  ```python
  is_superset = set2.issuperset(set1)  # True
  ```

- **Disjoint** (no common elements):

  ```python
  set3 = {5, 6}
  is_disjoint = set1.isdisjoint(set3)  # True
  ```

### 7. **Iterating Through a Set**

- **Iterate over elements**:

  ```python
  for item in my_set:
      print(item)
  ```

### 8. **Set Comprehensions**

- **Create a set from a list with a condition**:

  ```python
  numbers = [1, 2, 2, 3, 4, 5, 5, 6]
  unique_even_numbers = {x for x in numbers if x % 2 == 0}
  ```

### 9. **Conversion Between Lists and Sets**

- **Convert a list to a set (removes duplicates)**:

  ```python
  my_list = [1, 2, 2, 3, 4, 4]
  unique_set = set(my_list)  # Result: {1, 2, 3, 4}
  ```

- **Convert a set to a list**:

  ```python
  unique_list = list(unique_set)  # Converts back to list
  ```
