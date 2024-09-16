from django.db import models
from bs4 import BeautifulSoup
from .services import process_xml_file
from typing import Any
import os


class XmlDocument(models.Model):
    """
    This first model is use to upload xml file  by a client or admin site from database django interface

    """

    xml_file = models.FileField(upload_to="xml_files/")
    uploaded_xmlfile_at = models.DateTimeField(auto_now=True)

    def save(self, *args: Any, **kwargs: Any) -> None:

        # Save the instance first
        super().save(*args, **kwargs)

        # Call the external service to process the XML file
        process_xml_file(self.xml_file.path)

    def __str__(self):
        return f"Uploaded Xml file -> {os.path.basename(self.xml_file.path)} at {self.uploaded_xmlfile_at}"


class Content(models.Model):
    """
    This second model is use to store in database the content of xml file,
    in order to reconstruct the body of the document with its titles, paragraphs, etc.

    """

    content_document = models.TextField()
