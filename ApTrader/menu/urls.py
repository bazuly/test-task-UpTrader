from django.urls import path
from .views import Index

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("url/<url>/", Index.as_view(), name="menu_item"),
]
