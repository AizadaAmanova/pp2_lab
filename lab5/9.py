import re

s = "ThisIsATest"
pattern = r'([A-Z])' 

print(re.sub(pattern, r' \1', s).strip())
