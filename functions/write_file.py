import os

def write_file(working_directory, file_path, content):
    try:
        # get absolute path of working directory and target file
        wd_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(wd_path, file_path))

        # Is the target file within the working directory? It should be.
        # Will be True or False
        valid_file_path = os.path.commonpath([wd_path, target_file]) == wd_path

        # Check for valid arguments
        if valid_file_path is False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file) == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        parent_dir = os.path.dirname(target_file)
        os.makedirs(parent_dir, exist_ok=True)


        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: Could not write to "{file_path}": {e}'