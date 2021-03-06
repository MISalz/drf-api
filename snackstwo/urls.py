from django.urls import path
from .views import SnackDetail, SnackList

urlpatterns = [
  path("", SnackList.as_view(), name="snacks_two"),
  path("<int:pk>/", SnackDetail.as_view(), name="snacks_detail")
]