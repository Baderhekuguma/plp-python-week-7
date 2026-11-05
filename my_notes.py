# 1. Write three notes to a new file (overwriting if it already exists)
with open("my_notes.txt", "w") as f:
    f.write("Python is fun\n")
    f.write("Files are useful\n")
    f.write("Week 7 is going well\n")

# 2. Add a fourth note WITHOUT erasing the first three ("a" stands for append)
with open("my_notes.txt", "a") as f:
    f.write("I added this later\n")

# 3. Read the file back and print each line cleanly (strip removes extra blank lines)
print("--- My notes ---")
with open("my_notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# 4. Count the total lines in the file
with open("my_notes.txt", "r") as f:
    lines = f.readlines()
print("Total lines:", len(lines))