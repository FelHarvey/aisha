from functions.run_python_file import run_python_file

print("Calculator instructions")
print(run_python_file("calculator", "main.py"))

print("Run calculator... badly rendered")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("Run calculator tests")
print(run_python_file("calculator", "tests.py"))

print("Should return error")
print(run_python_file("calculator", "../main.py"))

print("Should return error")
print(run_python_file("calculator", "nonexistent.py"))

print("Should return error")
print(run_python_file("calculator", "lorem.txt"))