import requests
import os
import re

class GoogleDriveDownloader:
    def __init__(self):
        pass

    def download_file_from_link(self, file_link, destination_folder):
        """
        Download a file from a Google Drive link and save it to a specific destination folder
        with its original filename.

        :param file_link: The Google Drive file link.
        :param destination_folder: The folder where the file will be saved.
        """
        try:
            # Extract the file ID from the link
            file_id = self._extract_file_id(file_link)
            if not file_id:
                raise ValueError("Invalid Google Drive link.")

            # Construct the download URL
            download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

            # Ensure the destination folder exists
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Start a session to handle cookies (for large files)
            session = requests.Session()

            # Download the file
            response = session.get(download_url, stream=True)
            response.raise_for_status()  # Raise an error for bad status codes

            # Extract the filename from the Content-Disposition header
            content_disposition = response.headers.get("Content-Disposition")
            if content_disposition:
                # Extract the filename using regex
                filename_match = re.findall('filename="(.+)"', content_disposition)
                if filename_match:
                    filename = filename_match[0]
                else:
                    # Fallback: Use a default filename if extraction fails
                    filename = f"file_{file_id}"
            else:
                # Fallback: Use a default filename if no Content-Disposition header is found
                filename = f"file_{file_id}"

            # Full path to save the file
            output_path = os.path.join(destination_folder, filename)

            # Save the file to the specified output path
            with open(output_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print(f"File downloaded successfully to {output_path}")

        except Exception as e:
            print(f"Failed to download file: {e}")

    def _extract_file_id(self, file_link):
        """
        Extract the file ID from a Google Drive link.

        :param file_link: The Google Drive file link.
        :return: The file ID or None if the link is invalid.
        """
        if "file/d/" in file_link:
            # Link format: https://drive.google.com/file/d/FILE_ID/view
            start_index = file_link.find("file/d/") + len("file/d/")
            end_index = file_link.find("/", start_index)
            return file_link[start_index:end_index] if end_index != -1 else file_link[start_index:]
        elif "id=" in file_link:
            # Link format: https://drive.google.com/open?id=FILE_ID
            start_index = file_link.find("id=") + len("id=")
            end_index = file_link.find("&", start_index)
            return file_link[start_index:end_index] if end_index != -1 else file_link[start_index:]
        else:
            return None


