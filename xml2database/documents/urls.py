from django.urls import path
from .views import ContentListView

urlpatterns = [
    path("api/contents/", ContentListView.as_view(), name="content-list"),
]
