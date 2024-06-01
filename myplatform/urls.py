from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/users/', include('users.urls')),
    path('api/problems/', include('problems.urls')),
    path('', RedirectView.as_view(url='/api/auth/login/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
