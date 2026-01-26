from functions.get_file_content import get_file_content

print("Result for Lorem Ipsum")
print(get_file_content("calculator", "lorem.txt"))

print("Result for Calculator Main")
print(get_file_content("calculator", "main.py"))

print("Result for Calculator PKG")
print(get_file_content("calculator", "pkg/calculator.py"))

print("Result for bin/cat")
print(get_file_content("calculator", "/bin/cat"))

print("Result for nonexistent file")
print(get_file_content("calculator", "pkg/does_not_exist.py"))