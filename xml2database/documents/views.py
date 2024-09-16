from .models import Content
from rest_framework import generics
from .serializers import ContentSerializer


class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()  #  Retrieve all stored documents in database
    serializer_class = ContentSerializer
