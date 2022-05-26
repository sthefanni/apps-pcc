
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cursos/', include('cursos.urls')),
    path('conteudo/', include('conteudo.urls')),
    path('recursos/', include('recursos.urls')),
]
