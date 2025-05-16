def write_file(file_name, file_content):
    """
    Writes content to a .txt file
    
    Args:
        file_name (str): Name/path of the file (without .txt extension)
        file_content (str): Content to write to the file
    """
    with open(f"{file_name}.txt", 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    """
    Appends content to an existing .txt file
    
    Args:
        file_name (str): Name/path of the file (without .txt extension)
        append_content (str): Content to append to the file
    """
    with open(f"{file_name}.txt", 'a') as f:
        f.write(append_content)

def read_file(file_name):
    """
    Reads content from a .txt file
    
    Args:
        file_name (str): Name/path of the file (without .txt extension)
    
    Returns:
        str: Content of the file
    """
    with open(f"{file_name}.txt", 'r') as f:
        return f.read()