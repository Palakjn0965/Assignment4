with open("output.txt","at") as fobj:
    str1 = input(("Enter text to write to the file: "))
    fobj.write(str1)
    fobj.write("\n")
    print("Data successfully written to output.txt.")
    str2 = input("Enter additional text to append: ")
    fobj.write(str2)
    print("Data successfully appended.")

print("Final content of output.txt: ")
with open("output.txt","r") as fobj:
    lines = fobj.readlines()
    for line in lines:
        print(line.rstrip())