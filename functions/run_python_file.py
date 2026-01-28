import os, subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        # get absolute path of working directory and target file
        wd_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(wd_path, file_path))

        # Is the target file within the working directory? It should be.
        # Will be True or False
        valid_file_path = os.path.commonpath([wd_path, target_file]) == wd_path

        # Check for valid arguments
        if valid_file_path is False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_file) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if target_file.endswith('.py') == False:
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]

        if args is not None:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd = wd_path,
            capture_output= True,
            text = True,
            timeout= 30)
        
        output = []
        
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        
        if not result.stderr and not result.stdout:
            output.append("No output produced")
        else:
            if result.stdout:
                output.append(f"STDOUT:\n{result.stdout}")
            if result.stderr:
                output.append(f"STDERR:\n{result.stderr}")

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to run file from, relative to the working directory (default is the working directory itself)",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Any extra arguments",
                items=types.Schema(
                    type=types.Type.STRING
                )
            )
        },
        required=["file_path"]
    ),
)