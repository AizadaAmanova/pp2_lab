import re

text = ["ab", "acb", "a123b", "aXYZb", "a_b", "a-b", "a long text with b", 
        "b", "abc", "ba", "a", "babab", "a!@#b", "aaab", "a...b"]

pattern = r"^a.*b$"

for i in text:
    print(f"{i}: {bool(re.findall(pattern, i))}")
