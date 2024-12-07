from django.urls import path
from api import views


urlpatterns = [
    # Using Function-Based Views
    # path('', views.student_data),
    
    # Using Class-Based Views
    path('', views.StudentAPI.as_view()),
]
