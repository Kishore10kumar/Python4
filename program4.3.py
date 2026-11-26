try:
    s = input("Enter a string: ")

    if s == "":
        raise ValueError("String cannot be empty!")

    elif s == s[::-1]:
        print("Palindrome")

    else:
        print("Not a palindrome")

except ValueError as e:
    print(e)
