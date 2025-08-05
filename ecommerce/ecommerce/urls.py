from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ecommerceapp.urls")),
    path('auth/', include("authcart.urls")),
]

# ✅ Serve media files during development and on Render
if settings.DEBUG or os.environ.get('RENDER'):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
