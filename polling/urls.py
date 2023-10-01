from django.urls import path, include
from .views import PollListView, PollDetailView

urlpatterns = [
    path('', PollListView.as_view(), name="poll_index"),
    path('polls/<int:pk>/', PollDetailView.as_view(), name="poll_detail"),
]
