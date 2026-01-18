import os
file_name = "sample.txt"
if os.path.exists(file_name):
    with open("sample.txt","rt") as fobj:
        print("Reading file content:")
        lines = fobj.readlines()
        i=1
        for line in lines:
            print(f"Line {i}: {line.rstrip()}")
            i+=1
else:
    print(f"Error: The file {file_name} was not found.")