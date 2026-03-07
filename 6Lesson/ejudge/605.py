s = input()

vowels = "aeiouAEIOU"

if any(ch in vowels for ch in s):
    print("Yes")
else:
    print("No")