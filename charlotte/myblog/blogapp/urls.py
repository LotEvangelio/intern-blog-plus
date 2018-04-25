from django.urls import path
from . import views
from .views import PostDetailView, PostView

app_name = 'blogapp'

urlpatterns = [
    path('<title>', PostDetailView.as_view(), name='post_detail'),
    path('', PostView.as_view(), name='post'),
]