import re

text = ["SplitAtUppercaseLetters", "camelCaseExample", "PythonIsFun", "ThisIsATestString",
    "oneTwoThreeFour", "NoUppercase", "UPPERlowerUPPERlower", "HTMLParserFunction",
    "snake_case_example", "JSONDataProcessing" ]

pattern = r'(?=[A-Z])'

for i in text:
    print(f"{i}: {(re.split(pattern, i))}")