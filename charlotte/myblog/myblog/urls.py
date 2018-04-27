from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from user.views import RegisterView
from django.contrib.auth import get_user_model
User = get_user_model()
from user.views import RegisterView

urlpatterns = [
    path('posts/', include('blogapp.urls', namespace='posts')),
    path('admin/', admin.site.urls),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(model=User, success_url="/accounts/login/"), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)