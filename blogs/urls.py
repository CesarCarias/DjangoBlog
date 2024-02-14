from django.urls import path
from blogs.views import *

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
]