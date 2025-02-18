import os


class DirectoryScanner:
    def __init__(self, file_extensions):
        """
            This function is a constructor for the DirectoryScanner with specified file extensions.
            :param file_extensions: List of file extensions to scan for.
            :return: None
        """
        self.__file_extensions = file_extensions

    def scan(self, dir_name: str):
        """
           This function scans the directory and its subdirectories for files with the specified extensions.
            :param dir_name: Path to the directory to scan.
            :return: List of matching files with full file paths.
        """
        matching_files = []

        # Going over the directory and subdirectories
        for root, dirs, files in os.walk(dir_name):
            for file in files:
                if DirectoryScanner.is_extension_found(file, self.__file_extensions):
                    # Append the full file path to the list if extension was found
                    matching_files.append(os.path.join(root, file))

        return sorted(matching_files)

    def is_extension_found(file_name, file_extensions):
        """
            This function checks if the file's extension is in the list of file extensions.
            :param file_name: Name of the file to check.
            :param file_extensions: List of extensions to match against.
            :return: True if the file's extension matches, otherwise False.
        """
        extension = os.path.splitext(file_name)[1][1:]
        return extension in file_extensions

    def delete_file(self, file_path):
        """
            Thus function deletes the specified file from the system.
            :param file_path: Path of the file to delete.
            :return: Path of the deleted file if successful, otherwise None.
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File {file_path} was deleted successfully.")
                return file_path
            else:
                print(f"Error: {file_path} does not exist.")
        except PermissionError:
            print(f"Error: Permission denied while trying to delete: {file_path}")
        except Exception as e:
            print(f"Error: Could not delete {file_path} due to {e}")
