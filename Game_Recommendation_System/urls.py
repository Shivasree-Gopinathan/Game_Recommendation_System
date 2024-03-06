from django.contrib import admin
<<<<<<< Updated upstream
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
=======
from django.urls import path, include
from homepage import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('homepage.urls')),
    path('game/', include('game.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> Stashed changes
