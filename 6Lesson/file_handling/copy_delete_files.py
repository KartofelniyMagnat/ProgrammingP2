import os
import shutil


with open("sample.txt", "a", encoding="utf-8") as file:
    file.write("Grapes\n")
    file.write("Mango\n")

print("New lines appended.\n")

with open("sample.txt", "r", encoding="utf-8") as file:
    print("Updated file contents:")
    print(file.read())


shutil.copy("sample.txt", "sample_copy.txt")
shutil.copy("sample.txt", "sample_backup.txt")

print("Files copied: sample_copy.txt and sample_backup.txt\n")

for filename in ["sample_copy.txt", "sample_backup.txt"]:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted safely.")
    else:
        print(f"{filename} does not exist.")