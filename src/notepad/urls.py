from .views import create_view
from django.conf.urls import url

app_name = 'notes'

urlpatterns = [
    url(r'^create/', create_view, name='create'),
]
