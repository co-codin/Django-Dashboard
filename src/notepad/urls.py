from .views import create_view, list_view
from django.conf.urls import url

app_name = 'notes'

urlpatterns = [
    url(r'^create/', create_view, name='create'),
    url(r'^list', list_view, name='list')
]
