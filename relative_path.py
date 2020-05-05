import os.path

path = os.path.abspath(os.path.dirname(__file__))

print(path)

file_name = r"mySpecial/filename"

print(file_name)

full_path = os.path.join(path, file_name)

print(full_path)