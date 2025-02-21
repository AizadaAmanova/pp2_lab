import re

s = "ThisIsATest"
pattern = r'([A-Z])'

print(re.sub(pattern, r'_\1', s).lower().strip('_'))
