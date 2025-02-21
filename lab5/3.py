import re
text = ["my_variable test_case example_data", "no_match_here another_example", "No_match_here"]
pattern = r"\b[a-z]+_[a-z]+\b"
for i in text:
    print(f"{i}: {bool(re.findall(pattern, i))}")
