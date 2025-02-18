import os
from detector import FileReputation
from scanner import DirectoryScanner
from window import WarningWindow


class AntiVirus:
    def __init__(self, detector, scanner, window):
        self.__detector = detector
        self.__scanner = scanner
        self.__window = window

    def run(self):
        """
        This function runs the antivirus scan process. The user enters directory path, scans the directory for files,
        checks each file for malicious content, shows a warning if a malicious file is found, and deletes malicious files.
        :return: None
        """
        # Receiving input from the user
        dir_path = input("Enter the path to the directory you want to scan: ")

        # Scanning the directory for files with the given extensions
        files = self.__scanner.scan(dir_path)
        print(f"Scanning {dir_path}...")

        # Going over each file found by the scanner
        for file in files:
            print(f"Checking file: {file}")

            # Checking if the file is malicious using the function in the detector class( is_malicious function)
            if self.__detector.is_malicious(file):
                print(f"Malicious file found: {file}")

                # If the file is malicious show warning sign using WarningWindow class
                self.__window = WarningWindow(file)
                self.__window.show_window()

                self.__scanner.delete_file(file)
            else:
                print(f"File is safe: {file}")
        print("Scan completed!")


if __name__ == "__main__":
    detector = FileReputation()
    scanner = DirectoryScanner(['exe', 'txt', 'dll'])  # File extensions to scan for
    window = None

    antivirus = AntiVirus(detector, scanner, window)
    antivirus.run()
