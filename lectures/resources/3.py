import chardet

file_path = input("Enter your CSV file path: ").strip()

with open(file_path, 'rb') as f:
    rawdata = f.read(10000)
    result = chardet.detect(rawdata)

print("Detected encoding:", result['encoding'])

