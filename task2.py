write = input("Enter text to write to the file: ")

file = open("output.txt", "a")
print(file.write(write))
file.close()

print("Data successfully written to output.txt")


append = input("Enter additional text to append: ")

file = open("output.txt", "a")
print(file.write(append))
file.close()

print("Data successfully appended")

file = open("output.txt", "r")
print(file.read())
file.close()
