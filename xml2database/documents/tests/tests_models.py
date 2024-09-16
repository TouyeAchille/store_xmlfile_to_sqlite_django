from django.test import TestCase
from documents.models import XmlDocument, Content
from django.core.files.uploadedfile import SimpleUploadedFile
import os


class XmlDocumentModelTest(TestCase):
    def setUp(self):
        # Setup a fake XML file for testing
        self.xml_content = b"<root><contenu>afnor test technique</contenu></root>"
        self.xml_file = SimpleUploadedFile(
            "test.xml", self.xml_content, content_type="text/xml"
        )

    def test_xml_document_creation(self):
        # Create an XmlDocument instance and save it
        xml_document = XmlDocument.objects.create(xml_file=self.xml_file)

        # Check that the XML file is correctly saved
        self.assertTrue(os.path.exists(xml_document.xml_file.path))

        # Check that the content is correctly extracted and stored in the database
        content = Content.objects.first()
        self.assertIsNotNone(content)
        self.assertEqual(content.content_document, "afnor test technique")
