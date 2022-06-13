from django.urls import path
from .views import StickyListView, UploadView

urlpatterns = [
    path('', StickyListView.as_view()),  # sticky list
    path('upload/', UploadView.as_view()),  # upload stickies
]
