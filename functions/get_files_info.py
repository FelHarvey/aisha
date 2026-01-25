import os

def get_files_info(working_directory, directory="."):
    try:
        # get absolute path of working directory
        wd_path = os.path.abspath(working_directory)

        # get path to target directory
        target_dir = os.path.normpath(os.path.join(wd_path, directory))

        # Is the target directory within the working directory? It should be.
        # Will be True or False
        valid_target_dir = os.path.commonpath([wd_path, target_dir]) == wd_path

        # Check for valid arguments
        if valid_target_dir is False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isdir(target_dir) == False:
            return f'Error: "{directory}" is not a directory'
    
        contents_list = []

        # Populate list
        for f in os.listdir(target_dir):
            # Format
            # - README.md: file_size=1032 bytes, is_dir=False
            
            size = os.path.getsize(os.path.join(target_dir, f))
            is_dir = os.path.isdir(os.path.join(target_dir, f))

            temp_string = f"- {f}: file_size={size}, is_dir={is_dir}"
            
            contents_list.append(temp_string)

        return "\n".join(contents_list)

    except Exception as e:
        return f"Error: Something unexpected went wrong: {e}"


