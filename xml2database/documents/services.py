from bs4 import BeautifulSoup
from django.apps import apps
from pathlib import Path
from typing import Union
import os


def process_xml_file(file_path: Union[str, Path]) -> None:
    """
    This function processes the uploaded XML file, checks if the file exists,
    and extracts its content.

    """
    Content = apps.get_model("documents", "Content")

    # Convert the path to a Path object if it is a string
    file_path = Path(file_path) if isinstance(file_path, str) else file_path

    # checks if the file exists
    if not os.path.exists(file_path):
        raise ValueError(f"File not found: {file_path}")

    if not os.path.isfile(file_path):
        raise ValueError(f"Invalid file path: {file_path} is not a file.")

    _, file_extension = os.path.splitext(file_path)

    if file_extension.lower() != ".xml":
        raise ValueError(
            f"Invalid file extension: {file_extension}. Expected a .xml file."
        )

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            xml_content = file.read()

        soup = BeautifulSoup(xml_content, "lxml")
        contenu = soup.find("contenu")

        # Upload the content to the database
        if contenu:
            Content.objects.create(content_document=contenu.text)
        else:
            raise ValueError("Tag <contenu> not found in the XML file.")

    except Exception as e:
        # Handle errors like missing file or XML parsing issues
        raise ValueError(f"Error while processing the XML file: {e}")
