from django.urls import path
from .import views
from .views import PostDetailView, PostView

app_name = 'blogapp'

urlpatterns = [
    path('detail/<title>', PostDetailView.as_view(), name='post_detail'),
    path('', PostView.as_view(), name='post-list'),
    path('hidden/', views.Hidden, name='hidden'),
    path('draft/', views.Draft, name='draft'),
    path('<int:pk>/', views.comment, name='post-comment'),
]