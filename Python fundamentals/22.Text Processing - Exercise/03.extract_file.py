import os

path = input()
name = ""
something = "\\"
filename, file_extension = os.path.splitext(path)
for k in range(len(filename) - 1, -1, -1):
    if filename[k] != something:
        name += filename[k]
    else:
        break
name = name[::-1]
file_extension = file_extension[1::]

print(f"File name: {name}")
print(f"File extension: {file_extension}")