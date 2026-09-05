"""
7_context-managers.py

Rearranged to the topic template. Narrative lines converted to comments; original code blocks left unchanged.
"""

# 1. Concept (What it is)
# Context Managers: A context manager automatically handles setup and cleanup of a resource.
# The most common example is working with files.

# 2. Why AI engineers use it
# Ensures resources (files, DB connections, locks, GPUs) are reliably cleaned up even on errors.

# 3. Syntax
# with RESOURCE as VARIABLE:
#     # use the resource
# or implement __enter__ and __exit__ on a class, or use @contextmanager from contextlib.

# 4. Example (kept exactly as originally authored)

# Problem example (explicit open/close):
file = open("data.txt", "w")

file.write("Hello Python")

file.close()

# Safer pattern using with (file will be closed automatically):
with open("data.txt", "w") as file:
    file.write("Hello Python")

# What happens after the with block? The file is closed before execution continues.

# Enter/Exit conceptual methods used by context managers:
# __enter__() and __exit__()

class MyContext:
    def __enter__(self):
        print("Entering")
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")

with MyContext():
    print("Inside")

# __exit__ receives (exc_type, exc_value, traceback) indicating whether an exception occurred.

# Useful context manager example returning a value via __enter__:
class Demo:
    def __enter__(self):
        return "Hello"
    def __exit__(self, exc_type, exc_value, traceback):
        pass

with Demo() as value:
    print(value)  # prints Hello

# Context manager for a resource (e.g., database):
class Database:
    def __enter__(self):
        print("Connecting to database")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database")

with Database() as db:
    print("Using database")

# 5. contextlib usage (decorator + generator style)
from contextlib import contextmanager

@contextmanager
def demo():
    print("Starting")
    yield
    print("Finished")

with demo():
    print("Inside")

# 6. yield in a context manager: the yield pauses and resumes around the with block.

# 7. Why AI Engineers should know this
# In AI projects you work with files, DB connections, model/GPU resources, locks, temp files, network
# Use pattern: acquire -> operate -> release. Context managers enforce release.

# Important distinction (commented for clarity):
# Iterable: can be looped over (e.g., [1,2,3])
# Iterator: produces values one at a time (iter([1,2,3]))
# Context Manager: manages setup/cleanup (with open('file')...)

# --- Mini Practice (all) ---
# MP1: Create a file using with and write/read it.
with open('7_file-for-cm.txt', 'w') as f:
    f.write('Jobin Godson')
with open('7_file-for-cm.txt', 'r') as f:
    print(f.read())

# MP2: Create MyContext that prints entering/leaving
class MyContext2:
    def __enter__(self):
        print("entering context")
    def __exit__(self, exec_type, exec_value, traceback):
        print("leaving context")

with MyContext2():
    print("Inside context")

# MP3: Modify context manager so __enter__ returns a value
class MycontextReturn:
    def __enter__(self):
        print("entering context")
        return "Try removing the return statement and play around or put it in __exit__"
    def __exit__(self, exec_type, exec_value, traceback):
        print("leaving context")

with MycontextReturn() as value:
    print(value)

# MP4: Put an intentional error inside your context and observe __exit__ still runs
class MyContextError:
    def __enter__(self):
        print("entering context")
    def __exit__(self, exec_type, exec_value, traceback):
        print("leaving context")

try:
    with MyContextError():
        print("Inside")
        10 / 0
except Exception as e:
    print('Caught exception:', type(e).__name__)

# --- Assignments (solutions present in original file; kept intact) ---
# Assignment 1: File Handling
with open("7_data.txt", "w") as file:
    file.write("Python is easy to learn.\n")
    file.write("Context managers handle resources.\n")
    file.write("The with statement automatically closes the file.")

with open("7_data.txt", "r") as file:
    contents = file.read()

print(contents)

# Assignment 2: FileProcessor context manager
class FileProcessor:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, "r")
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        self.file.close()

with FileProcessor("7_data.txt") as file:
    print("Processing file...")
    data = file.read()
    print(data)