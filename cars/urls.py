from django.urls import path
from .views import CarView, CarDetailView

urlpatterns = [
    path("", CarView.as_view()),
    path("<int:car_id>", CarDetailView.as_view()),
]