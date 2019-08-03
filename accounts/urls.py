from django.urls import path
from .views import user_register_view

app_name = 'accounts'

urlpatterns = [
    path('register/',user_register_view,name='register_view')
]
