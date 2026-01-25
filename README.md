# Assignment4

Purpose:  
This program reads the contents of a text file and displays each line.

How it works:
- The 'os' module is imported to check whether the file exists.
- The program checks if 'sample.txt' is present using os.path.exists()'.
- If the file exists:
  - The file is opened in read mode ('rt').
  - All lines are read using 'readlines()'.
  - Each line is printed along with its line number.
- If the file does not exist:
  - An error message is displayed.

4. File Writing and Appending Program

Purpose:
This program writes text to a file, appends additional text, and then displays the final content of the file.

How it works:
- The file 'output.txt' is opened in append mode ('at').
- The user enters text which is written to the file.
- A newline character is added after writing.
- The user enters additional text which is appended to the same file.
- The file is then opened in read mode.
- The final content of the file is displayed line by line.
