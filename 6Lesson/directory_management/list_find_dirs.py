import os
print("Files and folders in current directory:")
for item in os.listdir("."):
    print(item)

print("\nFiles with .txt extension:")
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))