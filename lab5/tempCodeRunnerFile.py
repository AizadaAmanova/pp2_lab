for i in text:
    print(f"{i}: {(re.sub(pattern, ':', i))}")