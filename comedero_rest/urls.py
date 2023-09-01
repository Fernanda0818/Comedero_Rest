from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path,re_path
from django.views.static import serve

from apps.users.api import UserAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import Login,Logout



urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('login/',Login.as_view(), name = 'login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/',include('apps.users.routers')),
    path('api/', include('apps.Mascota.urls')),
    # path('usuario/', UserAPIView.as_view(), name='usuario_api'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)