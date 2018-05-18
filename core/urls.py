from django.urls import path

from . import views


urlpatterns = [
    path('', views.Ci.as_view()),
    path('<int:pk>', views.CiDetail.as_view()),
]
