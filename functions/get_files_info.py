import os

# Result for current directory:
#   - main.py: file_size=719 bytes, is_dir=False
#   - tests.py: file_size=1331 bytes, is_dir=False
#   - pkg: file_size=44 bytes, is_dir=True



def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    

    abs_directory = os.path.abspath(os.path.join(working_directory,directory))
    


    if not abs_directory.startswith(abs_working_directory):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    

    final_responce = ""
    contents = os.listdir(abs_directory)
    
    for content in contents:
        content_path = os.path.join(abs_directory,content)

        is_dir = os.path.isdir(content_path)
        file_size = os.path.getsize(content_path)
        final_responce += f"-{content} file_size={file_size} bytes, is_dir={is_dir}\n"
    return final_responce