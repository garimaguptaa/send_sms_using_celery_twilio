from django.urls import path, include
from .views import MeetingViewset

# the api urls are now determined automatically by the router.
urlpatterns = [
    path('reciepients/', MeetingViewset.as_view()),
]