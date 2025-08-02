from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.contact),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
