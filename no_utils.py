"""
no_utils.py

This module provides varios utilities for performing common tasks such as executing system commands, 
guarding against None and empty variables, and manipulating files.
"""

import sys
from subprocess import Popen, PIPE

def system_cmd(command):
    """
    Execute a system command and return its exit code, standard output, and standard error.

    Parameters:
    - command (str): The system command to execute.

    Returns:
    - tuple: A tuple containing the exit code (int), standard output (str), and standard error (str).
    """
    with Popen(args=command, stdout=PIPE, stderr=PIPE, shell=True) as process:
        out, err = process.communicate()
        retcode = process.poll()
    return retcode, out.decode("utf-8"), err.decode("utf-8")

class Guard:
    """
    A utility class for guarding against None and empty variables.

    Methods:
    - against_none(var, force_exit=True): Check if the variable is None and optionally exit the program.
    - against_empty(var, force_exit=True): Check if the variable is empty and optionally exit the program.
    """

    def against_none(self, var, force_exit=True):
        """
        Check if the variable is None and optionally exit the program.

        Parameters:
        - var: The variable to check.
        - force_exit (bool): Whether to exit the program if the variable is None. Default is True.
        """
        if var is None:
            print("Supplied variable is None!")
            if force_exit:
                sys.exit(-1)

    def against_empty(self, var, force_exit=True):
        """
        Check if the variable is empty and optionally exit the program.

        Parameters:
        - var: The variable to check. Can be a list, dict, set, or tuple.
        - force_exit (bool): Whether to exit the program if the variable is empty. Default is True.
        """
        if isinstance(var, list):
            var_type = "list"
        elif isinstance(var, dict):
            var_type = "dict"
        elif isinstance(var, set):
            var_type = "set"
        elif isinstance(var, tuple):
            var_type = "tuple"
        else:
            var_type = None

        if var_type:
            is_empty = len(var) == 0
            if is_empty:
                print(f"Supplied variable of type {var_type} is empty!")
                if force_exit:
                    sys.exit(-1)

class FileUtils:
    """
    A utility class for performing various file operations such as replacing text,
    clearing content, appending data, checking for content existence, and manipulating lines.

    Methods:
    - replace(file_path, old_str, new_str, encoding='utf-8'): Replace occurrences of old_str with new_str in the specified file.
    - clear(file_path, encoding='utf-8'): Clear the content of the specified file.
    - append(file_path, data, encoding='utf-8'): Append data to the specified file.
    - content_exists(file_path, content, encoding='utf-8'): Check if the specified content exists in the file.
    - get_lines_with_content(file_path, content, encoding='utf-8'): Get lines from the file that contain the specified content.
    - get_lines_without_content(file_path, content, encoding='utf-8'): Get lines from the file that do not contain the specified content.
    - remove_empty_lines(file_path, encoding='utf-8'): Remove all empty lines from the specified file.
    - remove_last_empty_line(file_path, encoding='utf-8'): Remove the last empty line from the specified file.
    """
    def replace(self, file_path, old_str, new_str, encoding='utf-8'):
        """Replace occurrences of old_str with new_str in the specified file."""
        with open(file_path, 'r', encoding=encoding) as file:
            filedata = file.read()

        newdata = filedata.replace(old_str, new_str)

        with open(file_path, 'w', encoding=encoding) as file:
            file.write(newdata)
    
    def clear(self, file_path, encoding='utf-8'):
        """Clear the content of the specified file."""
        with open(file_path, 'w', encoding=encoding) as file:
            file.write("")
    
    def append(self, file_path, data, encoding='utf-8'):
        """Append data to the specified file."""
        with open(file_path, 'a', encoding=encoding) as file:
            file.write(data)
    
    def content_exists(self, file_path, content, encoding='utf-8'):
        """Check if the specified content exists in the file."""
        with open(file_path, 'r', encoding=encoding) as file:
            filedata = file.read()
        
        return content in filedata
    
    def get_lines_with_content(self, file_path, content, encoding='utf-8'):
        """Get lines from the file that contain the specified content."""
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
        
        return [line for line in lines if content in line]
    
    def get_lines_without_content(self, file_path, content, encoding='utf-8'):
        """Get lines from the file that do not contain the specified content."""
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
        
        return [line for line in lines if content not in line]
    
    def remove_empty_lines(self, file_path, encoding='utf-8'):
        """Remove all empty lines from the specified file."""
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
        
        lines = [line for line in lines if line.strip() != ""]
        
        with open(file_path, 'w', encoding=encoding) as file:
            file.writelines(lines)
    
    def remove_last_empty_line(self, file_path, encoding='utf-8'):
        """Remove the last empty line from the specified file."""
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
        
        if lines and lines[-1].strip() == "":
            lines = lines[:-1]
        
        with open(file_path, 'w', encoding=encoding) as file:
            file.writelines(lines)
            if lines and lines[-1].strip() != "":
                file.write("\n")