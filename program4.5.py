s = input("Enter main string: ")
sub = input("Enter string to insert: ")
pos = input("Enter position: ")

if s == "" or sub == "":
    print("Strings cannot be empty!")
elif not pos.isdigit():
    print("Invalid position!")
elif int(pos) > len(s):
    print("Position out of range!")
else:
    pos = int(pos)
    print("New string:", s[:pos] + sub + s[pos:])
