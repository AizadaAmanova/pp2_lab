import re

text = ["Hello, world. This is a test", "Python,Java.C++ JavaScript", "Replace, all. spaces, and.dots",
    "NoPunctuationHere", " , . , , . . ", "Comma,period.space test", "One sentence. Another one, and another.",
    "Python is fun, but C++ is tricky.", "Replace   multiple    spaces too.", "123,456.789 test,123.456",]

pattern = r'[ ,.]'

for i in text:
    print(f"{i}: {(re.sub(pattern, ':', i))}")
