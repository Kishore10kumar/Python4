main = input("Enter main string: ")
sub = input("Enter sub-string: ")

if main == "" or sub == "":
    print("Strings cannot be empty!")
else:
    found = False

    for i in range(len(main) - len(sub) + 1):
        if main[i:i+len(sub)] == sub:
            print("Found at position", i)
            found = True

    if not found:
        print("Sub-string not found")
