from django.contrib import admin
from django.urls import path, include
from AppRequerimientos import urls
from django.conf.urls.static import static
from django.conf import settings
from AppRequerimientos.views import rndr_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rndr_home, name='Home'),
    path('requerimientos/', include('AppRequerimientos.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Procesos de asignación de pedidos, carga y servicio de imágenes"
admin.site.site_title = "PROCESOS DE ASIGNACIÓN DE PEDIDOS"