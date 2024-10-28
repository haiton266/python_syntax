Here’s a quick reference for handling lists in Python, specifically tailored for coding competitions like Codeforces:

### 1. **Creating a List**

- **Empty list**:

  ```python
  my_list = []
  ```

- **List with initial elements**:

  ```python
  my_list = [1, 2, 3, 4, 5]
  ```

### 2. **Accessing and Modifying Elements**

- **Access an element by index**:

  ```python
  first_element = my_list[0]  # First element
  last_element = my_list[-1]  # Last element
  ```

- **Modify an element by index**:

  ```python
  my_list[0] = 10
  ```

### 3. **List Operations**

- **Add elements**:

  ```python
  my_list.append(6)        # Add to the end
  my_list.insert(0, 0)     # Insert at index 0
  ```

- **Remove elements**:

  ```python
  my_list.pop()            # Remove last element
  my_list.pop(0)           # Remove element at index 0
  my_list.remove(3)        # Remove first occurrence of 3
  ```

- **Length of the list**:

  ```python
  length = len(my_list)
  ```

### 4. **List Iteration**

- **Iterate over elements**:

  ```python
  for item in my_list:
      print(item)
  ```

- **Iterate with index**:

  ```python
  for index, item in enumerate(my_list):
      print(index, item)
  ```

### 5. **List Slicing**

- **Basic slicing**:

  ```python
  sublist = my_list[1:4]   # Elements from index 1 to 3
  ```

- **Step slicing**:

  ```python
  every_other = my_list[::2]  # Every second element
  reversed_list = my_list[::-1]  # Reverse the list
  ```

### 6. **List Functions**

- **Find the maximum and minimum**:

  ```python
  max_value = max(my_list)
  min_value = min(my_list)
  ```

- **Sum of all elements**:

  ```python
  total = sum(my_list)
  ```

- **Check if an element exists**:

  ```python
  if 3 in my_list:
      print("3 is in the list")
  ```

### 7. **List Methods**

- **Count occurrences of an element**:

  ```python
  count_of_3 = my_list.count(3)
  ```

- **Find the index of the first occurrence**:

  ```python
  index_of_4 = my_list.index(4)  # Raises an error if 4 is not found
  ```

- **Sort the list**:

  ```python
  my_list.sort()             # Sorts in-place, ascending
  my_list.sort(reverse=True) # Sorts in-place, descending
  ```

- **Sorted (without modifying original list)**:

  ```python
  sorted_list = sorted(my_list)
  ```

- **Reverse the list**:

  ```python
  my_list.reverse()          # In-place reversal
  reversed_list = my_list[::-1]  # Reversed copy
  ```

### 8. **List Comprehensions**

- **Create a list from another list**:

  ```python
  squares = [x * x for x in my_list]  # Square each element
  ```

- **With condition**:

  ```python
  even_numbers = [x for x in my_list if x % 2 == 0]  # Only even numbers
  ```

### 9. **Merging and Copying Lists**

- **Concatenate lists**:

  ```python
  list1 = [1, 2, 3]
  list2 = [4, 5, 6]
  combined = list1 + list2
  ```

- **Extend a list**:

  ```python
  list1.extend(list2)  # Adds elements of list2 to the end of list1
  ```

- **Copy a list**:

  ```python
  copied_list = my_list[:]   # Shallow copy
  copied_list = my_list.copy()  # Another way to shallow copy
  ```

### 10. **Using `collections.deque` for Efficient Operations**

- **Faster appending and popping from both ends**:

  ```python
  from collections import deque
  my_deque = deque([1, 2, 3, 4])
  my_deque.append(5)          # Add to the end
  my_deque.appendleft(0)      # Add to the beginning
  my_deque.pop()              # Remove from the end
  my_deque.popleft()          # Remove from the beginning
  ```

### 11. **Advanced: Using `heapq` for Min-Heaps**

- **Using a list as a min-heap**:

  ```python
  import heapq
  heap = [3, 2, 5, 1, 4]
  heapq.heapify(heap)           # Convert list to a heap
  heapq.heappush(heap, 0)       # Add element to the heap
  smallest = heapq.heappop(heap) # Remove and return the smallest element
  ```
