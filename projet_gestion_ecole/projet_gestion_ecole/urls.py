from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('gestion_ecole/admin/', admin.site.urls),
    path('gestion_ecole/', include('application_gestion_ecole.urls')),
    path('captcha/', include('captcha.urls')),
    path('ids-gestion_ecole/', include ( "django.contrib.auth.urls" )),
    path('', lambda request: redirect("gestion_ecole/",permament=False)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
