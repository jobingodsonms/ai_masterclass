#1 & 2. Importing from a Module & Importing Specific Functions from a Module

from utility.text_utils import clean_text, word_count, is_long_text
#import text_utils (commented)

text = input("enter a sentnce: ")
print("original text: ", text)

stores_clean = clean_text(text)
print("text converted to lower case: ", stores_clean)

count_var = word_count(text)
print("word count: ", count_var)

long = is_long_text(text)
print("is long text: ", long)


# 3. Importing from a Module with an Alias
import utility.math_utils as mat

print(mat.square(5))
print(mat.cube(5))


# 5. sentiment analysis using a function from a module

import utility.sentiment as sent

print(sent.simple_sentiment("I am very happy"))