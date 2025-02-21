import re

def to_camel(match):
    return match.group(1).upper()

s = "snake_case_example"
print(re.sub(r'_([a-z])', to_camel, s))