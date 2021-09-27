from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from .views import HomePage, HomePage1

urlpatterns = [
    path('idol/<int:pk>',HomePage,name='home'),
    path('idol/',HomePage1,name='home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)