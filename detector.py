from abc import ABC, abstractmethod
import hashlib
import requests


class Detector(ABC):
    @abstractmethod
    def calculate(self, file_name):
        raise NotImplementedError("Subclasses must implement calculate method")

    @abstractmethod
    def is_malicious(self, file_name):
        raise NotImplementedError("Subclasses must implement is_malicious method")


class FileReputation(Detector):
    def calculate(self, file_name):
        """
            This function calculates the hash of a file.
            :param file_name: The name of the file to calculate the hash for.
            :return: The hash of the file as a string.
        """
        with open(file_name, 'rb') as file:
            file_content = file.read()
        hash_object = hashlib.sha256(file_content)
        return hash_object.hexdigest()

    def send_vt_sha256(self, sha256):
        """
            This function sends the SHA-256 hash of a file to VirusTotal to check for malicious status.

            :param sha256: The SHA-256 hash of the file.
            :return: True if VirusTotal detects the file as malicious, False otherwise.
        """
        url = "https://www.virustotal.com/api/v3/files/" + sha256
        headers = {"accept": "application/json",
                   "x-apikey": "44fbb8757e3b5d3dc1bc4daa8ea7515e33638f9831670bbb78604e6e444c49d2"}
        response = requests.get(url, headers=headers)
        suspicious = (response.json()["data"]["attributes"]["last_analysis_stats"]["malicious"])
        return int(suspicious) > 0

    def is_malicious(self, file_name):
        """
            This function checks if a file is malicious.
            :param file_name: The name of the file to check.
            :return: True if the file is malicious, False otherwise.
        """
        # Test code for a specific file
        # if file_name.endswith("test_file.txt"):
        #    return True
        hash = self.calculate(file_name)
        return self.send_vt_sha256(hash)
