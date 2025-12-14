import re

class CText:
    def __init__(self, text):
        self.contents = text
        self.length = len(text)
        self.word_count = len(text.split())        
        self.paragraph_count = len(text.split(".")) 
    
    def describe(self):
        return f"The text contains: {self.length} characters, {self.word_count} words and {self.paragraph_count} paragraphs."

    def update_desription(self, text):
        self.length = len(text)
        self.word_count = len(text.split())        
        self.paragraph_count = len(text.split(".")) 

    def read(self):
        return self.contents
    
    def write_and_append(self, text_to_add):
        self.contents += (" " + text_to_add)
        self.update_desription(self.contents)
        return 1

    def write_and_replace(self, text_to_replace):
        self.contents = text_to_replace
        self.update_desription(self.contents)
        return 1
    
text1 = CText("This is a practice on regular expressions and strings.")
print(f"Initial string: {text1.read()}")
print(text1.describe())
print("*****")

text1.write_and_append("Which uses python programmin languege.")
print(f"Appended string: {text1.read()}")
print(text1.describe())
print("*****")

text1.write_and_replace("This sentence has replaced the old one.")
print(f"Replaced string: {text1.read()}")
print(text1.describe())
