### 1. **Input Reading**

- **Read a string**:

  ```python
  user_input = input()
  print(user_input)
  ```

- **Read an integer**:

  ```python
  number = int(input())
  print(number)
  ```

- **Read a floating-point number**:

  ```python
  float_number = float(input())
  print(float_number)
  ```

- **Read multiple integers on a single line** (separated by spaces):

  ```python
  a, b = map(int, input().split())
  print(a, b)
  ```

- **Read a list of integers** (all in one line, separated by spaces):

  ```python
  numbers = list(map(int, input().split()))
  print(numbers)
  ```

### 2. **Output**

- **Print a string**:

  ```python
  print("Hello, World!")
  ```

- **Print multiple values on the same line**:

  ```python
  name = "Alice"
  age = 25
  print(name, age)
  ```

- **Use `f-string` for formatted output** (Python 3.6+):

  ```python
  name = "Alice"
  age = 25
  print(f"Name: {name}, Age: {age}")
  ```

- **Use `format()` for string formatting**:

  ```python
  name = "Alice"
  age = 25
  print("Name: {}, Age: {}".format(name, age))
  ```

- **Format numbers with decimals**:

  ```python
  pi = 3.14159265359
  print("{:.2f}".format(pi))  # Output: 3.14
  ```

- **Print without a newline**:

  ```python
  for i in range(5):
      print(i, end=" ")  # Output: 0 1 2 3 4
  ```

### 3. **File Handling (if allowed in problem constraints)**

- **Write data to a file**:

  ```python
  with open("output.txt", "w") as file:
      file.write("Hello, World!")
  ```

- **Read data from a file**:

  ```python
  with open("output.txt", "r") as file:
      content = file.read()
      print(content)
  ```
