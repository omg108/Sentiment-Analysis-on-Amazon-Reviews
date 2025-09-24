# Regular Expressions (Regex) in Python

A **regular expression** (or **regex**) in Python is a **pattern** used to **search, match, or manipulate text**.  
Think of it as a powerful tool to find specific strings in text without checking each character manually.

---

## Example in Real Life
- You want to find all phone numbers in a text.
- Instead of checking every number manually, you can write a **pattern** that matches phone numbers.

---

## Example in Python

```python
import re

text = "My number is 9876543210"
pattern = r"\d{10}"  # \d means digit, {10} means exactly 10 digits

match = re.search(pattern, text)
if match:
    print("Found:", match.group())
```


Output:
  Found: 9876543210


-re.search() → finds the first match
-match.group() → gives the text that matched the pattern

Use Cases
-Validate emails, phone numbers, or passwords
-Find/replace text
-Extract specific patterns from documents or logs



### Explanation

- `\d` → Matches any **digit** (0-9)  
- `{10}` → Matches **exactly 10 digits** in a row  

Together, `\d{10}` matches any sequence of **10 consecutive digits**, which is typical for phone numbers.

---

## Match Found

- **Matched Text:** `9991116666`  
- **Position:** Characters 28 to 38 in the string  

---

## Python Example

```python
import re

text = "Elon musk's phone number is 9991116666, call him if you have any questions on dogecoin."
pattern = r"\d{10}"

match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())




