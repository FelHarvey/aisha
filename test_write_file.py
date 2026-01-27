from functions.write_file import write_file

print("Notation for Lorem Ipsum")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print("Create more Lorem")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print("Expected error")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))