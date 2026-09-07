## Modules & Packages Project — Summary

### Goal

Build a small **AI-style text processing project** to practice Python **modules, packages, imports, aliases, and `__name__ == "__main__"`**.

### Final Project Structure

```text
ai_text_project/
│
├── main.py
│
└── utility/
    ├── __init__.py
    ├── text_utils.py
    ├── math_utils.py
    └── sentiment.py
```

### 1. `text_utils.py`

Create three functions:

```text
clean_text(text)
    → lowercase + remove extra leading/trailing spaces

word_count(text)
    → count number of words

is_long_text(text)
    → True if more than 10 words
    → False otherwise
```

Also use:

```python
if __name__ == "__main__":
```

to test the functions when `text_utils.py` is run directly.

---

### 2. `math_utils.py`

Create:

```text
square(n) → n²
cube(n)   → n³
```

Practice importing it with an alias:

```text
math_utils → mathu
```

---

### 3. `sentiment.py` 

Create:

```text
simple_sentiment(text)
```

Rules:

```text
good, great, excellent, happy → Positive

bad, terrible, sad, hate → Negative

anything else → Neutral
```

---

### 4. `__init__.py`

Create it inside `utility/`.

For this project, **leave it empty**.

---

### 5. `main.py`

`main.py` should bring everything together.

It should:

```text
1. Ask the user for a sentence
          ↓
2. Clean the text
          ↓
3. Count the words
          ↓
4. Check whether it's long
          ↓
5. Determine sentiment
          ↓
6. Demonstrate square/cube
          ↓
7. Display the results
```

Example final output:

```text
Enter a sentence: I am very happy with this great project

Cleaned text: i am very happy with this great project
Word count: 8
Is long text: False
Sentiment: Positive
Square: 25
Cube: 125
```

### Concepts you're practicing

```text
Modules
   ↓
import
   ↓
from ... import
   ↓
as (alias)
   ↓
__name__ == "__main__"
   ↓
Packages
   ↓
__init__.py
   ↓
Multiple modules working together
```

**Don't focus on making the project advanced.** The main objective is to understand how `main.py` communicates with separate modules inside the `utility` package.