import os
import shutil

os.makedirs("practice/folder1", exist_ok=True)
os.makedirs("practice/folder2", exist_ok=True)

f = open("practice/folder1/example.txt", "w", encoding="utf-8") 
f.write()


f.close()
with open("practice/folder1/example.txt", "w", encoding="utf-8") as f:

    f.write("This is a sample file.")

shutil.copy("practice/folder1/example.txt", "practice/folder2/example_copy.txt")
print("File copied.")

shutil.move("practice/folder1/example.txt", "practice/folder2/example_moved.txt")
print("File moved.")