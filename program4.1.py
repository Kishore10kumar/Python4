s = input("Enter a string: ")

if s == "":
    print("String cannot be empty!")
elif s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
