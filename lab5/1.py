import re
text = ["ab","a","abc"]
pattern = r"^ab*"
for i in text:
    print(f"{i}: {bool(re.findall(pattern, i))}")
