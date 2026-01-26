import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        # get absolute path of working directory and target file
        wd_path = os.path.abspath(working_directory)
        target_file = os.path.abspath(os.path.join(wd_path, file_path))

        # Is the target file within the working directory? It should be.
        # Will be True or False
        valid_file_path = os.path.commonpath([wd_path, target_file]) == wd_path

        # Check for valid arguments
        if valid_file_path is False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_file) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
        
    except Exception as e:
        return f"Error: Something unexpected went wrong when trying to open {file_path}: {e}"