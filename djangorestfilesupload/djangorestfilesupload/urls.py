
from django.urls import include, path
from rest_framework import routers
from restfilesupload import views

router = routers.DefaultRouter()
router.register(r'', views.FileUploadViewSet, basename='')

urlpatterns = [
    #path('admin/', admin.site.urls),
	path('upload/', include(router.urls)),
]