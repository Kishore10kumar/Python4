s = input("Enter a string: ")

if s == "":
    print("String cannot be empty!")
else:
    words = s.split()
    print("Number of words =", len(words))
