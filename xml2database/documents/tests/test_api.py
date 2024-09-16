from rest_framework.test import APITestCase
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from documents.models import XmlDocument


class XmlDocumentAPITest(APITestCase):
    def setUp(self):
        # Setup a fake XML file for testing
        self.xml_content = b"<root><contenu>Some content in XML</contenu></root>"
        self.xml_file = SimpleUploadedFile(
            "test.xml", self.xml_content, content_type="text/xml"
        )

        # Create an XmlDocument instance
        self.xml_document = XmlDocument.objects.create(xml_file=self.xml_file)

    def test_get_xml_document(self):
        #  API urls
        url = "/documents/api/contents/?format=api"
        response = self.client.get(url)

        # Verify that the response is correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["content_document"], "Some content in XML")
