from django.urls import path
from . import views as vi



urlpatterns = [
    path('main/',vi.main), 
    path('login/',vi.login),
    path('reg/',vi.reg),
]
