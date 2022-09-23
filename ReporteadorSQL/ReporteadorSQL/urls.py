"""vulner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf  import settings
from django.conf.urls.static import  static


from Reportes import views

#from admisiones import views as viewsAdmisiones

#from usuarios import views as viewsUsuarios

from django.conf  import settings
from django.conf.urls.static import  static
#from clinico import views as viewsClinico
#from mecanicosPacientes import views as viewsmecanicosPacientes



urlpatterns = [
    path('admin/', admin.site.urls),

    # Primero Reporteador

    path('chaining/', include('smart_selects.urls')),
    path('medicalReport/', views.menuAcceso),
    path('validaAcceso/', views.validaAcceso),
    path('salir/', views.salir),
    path('pantallaSubgrupos/<str:username>, <str:sedeSeleccionada>, <str:grupo>', views.pantallaSubgrupos),
    path('emergenteGrupos/<str:username>, <str:sedeSeleccionada>, <str:grupo>', views.emergenteGrupos),
    path('combo/<str:username>, <str:sedeSeleccionada>, <str:grupo>, <str:subGrupo>', views.combo),
    path('/combo/<str:username>, <str:sedeSeleccionada>, <str:grupo>, <str:subGrupo>', views.combo),

    # path('contrasena/<str:documento>', views.contrasena),

    ## Invoca Reporte

    path('Reporte1/<str:numreporte>,<str:username>,<str:sedeSeleccionada>,<str:grupo>,<str:subGrupo>', views.Reporte1PdfView.as_view()),
    # path('Reporte2/<str:numreporte>,<str:username>,<str:sedeSeleccionada>,<str:grupo>,<str:subGrupo>', views.Reporte1PdfView.as_view()),

    # Fin Reporteador


]


if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

# Añadir
admin.site.site_header = 'Administracion Medical Report'
admin.site.site_title = "Portal de Medical Report"
admin.site.index_title = "Bienvenidos al portal de administración Medical Report"
