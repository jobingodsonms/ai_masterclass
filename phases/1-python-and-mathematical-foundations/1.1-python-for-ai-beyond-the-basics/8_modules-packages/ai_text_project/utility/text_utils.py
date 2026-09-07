# 4. use the __name__ variable

# if __name__ == "__main__":                    
# if __name__ == "__main__": is used to check whether the script is being run directly or being imported as a module.


def clean_text(text):
    return text.lower().strip()

def word_count(text):
    return len(text.split())

def is_long_text(text):
    return len(text.split()) > 10