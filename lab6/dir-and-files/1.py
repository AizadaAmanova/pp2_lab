import os

def list_full_path(path="."):
    items = os.listdir(path)
    for item in items:
        print(os.path.join(path, item))

list_full_path()