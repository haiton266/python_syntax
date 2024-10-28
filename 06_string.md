### 1. **Creating a String**

- **Simple string**:

  ```python
  my_string = "Hello, World!"
  ```

- **Multiline string**:

  ```python
  multiline_string = """This is
  a multiline
  string."""
  ```

### 2. **Accessing Elements**

- **Access a character by index**:

  ```python
  first_char = my_string[0]  # 'H'
  last_char = my_string[-1]  # '!'
  ```

- **String slicing**:

  ```python
  substring = my_string[0:5]  # 'Hello'
  ```

### 3. **String Operations**

- **Concatenate strings**:

  ```python
  str1 = "Hello"
  str2 = "World"
  result = str1 + " " + str2  # 'Hello World'
  ```

- **Repeat a string**:

  ```python
  repeated_string = "Hi! " * 3  # 'Hi! Hi! Hi! '
  ```

### 4. **String Methods**

- **Convert to lowercase/uppercase**:

  ```python
  lower_string = my_string.lower()  # 'hello, world!'
  upper_string = my_string.upper()  # 'HELLO, WORLD!'
  ```

- **Strip whitespace from the beginning and end**:

  ```python
  stripped_string = "  Hello  ".strip()  # 'Hello'
  ```

- **Replace substrings**:

  ```python
  replaced_string = my_string.replace("World", "Universe")  # 'Hello, Universe!'
  ```

- **Split a string into a list** (default: split by spaces):

  ```python
  words = my_string.split()  # ['Hello,', 'World!']
  ```

- **Join a list into a string**:

  ```python
  word_list = ['Hello', 'World']
  joined_string = " ".join(word_list)  # 'Hello World'
  ```

- **Count occurrences of a substring**:

  ```python
  count = my_string.count('l')  # 3
  ```

- **Find the index of the first occurrence of a substring**:

  ```python
  index = my_string.find('World')  # 7
  ```

### 5. **Checking Conditions**

- **Check if a string starts/ends with a substring**:

  ```python
  starts = my_string.startswith('Hello')  # True
  ends = my_string.endswith('!')          # True
  ```

- **Check if a substring exists**:

  ```python
  if 'World' in my_string:
      print("Found 'World'!")
  ```

- **Check if all characters are digits/letters/alphanumeric**:

  ```python
  is_digit = '12345'.isdigit()  # True
  is_alpha = 'Hello'.isalpha()  # True
  is_alnum = 'Hello123'.isalnum()  # True
  ```

### 6. **String Formatting**

- **Using `format()` method**:

  ```python
  name = "Alice"
  age = 25
  formatted_string = "Name: {}, Age: {}".format(name, age)  # 'Name: Alice, Age: 25'
  ```

- **Using f-strings** (Python 3.6+):

  ```python
  formatted_string = f"Name: {name}, Age: {age}"  # 'Name: Alice, Age: 25'
  ```

- **Formatting numbers**:

  ```python
  pi = 3.14159265
  formatted_pi = "{:.2f}".format(pi)  # '3.14'
  ```

### 7. **Reversing a String**

- **Reverse a string using slicing**:

  ```python
  reversed_string = my_string[::-1]  # '!dlroW ,olleH'
  ```

### 8. **Iterating Through a String**

- **Iterate over each character**:

  ```python
  for char in my_string:
      print(char)
  ```

### 9. **String Comparisons**

- **Compare two strings** (lexicographical order):

  ```python
  result = "apple" < "banana"  # True
  ```

### 10. **String Slicing and Substring Operations**

- **Extract a substring**:

  ```python
  my_substring = my_string[1:5]  # 'ello'
  ```

- **Step slicing**:

  ```python
  stepped_string = my_string[::2]  # 'Hlo ol!'
  ```

### 11. **Convert Between Strings and Lists**

- **Convert a string to a list of characters**:

  ```python
  char_list = list(my_string)  # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
  ```

- **Convert a list of characters back to a string**:

  ```python
  new_string = ''.join(char_list)  # 'Hello, World!'
  ```

### 12. **Useful Tips for Competitions**

- **Strings are immutable** in Python, so you can't modify them directly. You have to create new strings instead.
- **Use slicing and built-in methods for efficient operations**. For example, `in` is very fast for checking substrings.

- **Use `join()` over `+` for concatenating large strings** in loops, as it's much more efficient.

### 13. **Advanced String Techniques**

- **Removing non-alphanumeric characters**:

  ```python
  clean_string = ''.join(c for c in my_string if c.isalnum())  # Removes spaces, punctuation
  ```

- **Converting between ASCII and characters**:

  ```python
  char = chr(65)  # 'A'
  ascii_value = ord('A')  # 65
  ```

### 14. **Multiline Strings**

- **Using triple quotes for multiline strings**:

  ```python
  multi_line_str = """This is
  a string
  that spans multiple lines."""
  ```
