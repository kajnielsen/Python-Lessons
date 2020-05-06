import os.path

path = os.path.abspath(os.path.dirname(__file__))

print(path)

file_name = "pythonClass.db"

print(file_name)

full_path = os.path.join(path, file_name)

print(full_path)