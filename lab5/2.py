import re
text = ["abc","aabb","abb", "acc"]
pattern = r"^ab{2,3}"
for i in text:
    print(f"{i}: {bool(re.findall(pattern, i))}")
