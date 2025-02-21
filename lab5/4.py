import re

text = ["Hello", "world", "Python", "AI", "MachineLearning", "Data_Science", 
        "Regex", "java", "C++", "Abc", "Test1", "X", "UpperCASE", "GoodMorning"]

pattern = r"\b[A-Z][a-z]"

for i in text:
    print(f"{i}: {bool(re.findall(pattern, i))}")
