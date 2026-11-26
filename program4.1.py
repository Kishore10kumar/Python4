s = input("Enter a string: ")

if s == "":
    print("String cannot be empty!")
else:
    i = 0
    j = len(s) - 1
    palin = True
    while i < j:
        if s[i] != s[j]:
            palin = False
            break
        i = i + 1
        j = j - 1
    if palin:
        print("Palindrome")
    else:
        print("Not a palindrome")
