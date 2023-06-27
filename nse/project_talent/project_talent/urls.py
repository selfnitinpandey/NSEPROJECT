from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from app.views import NoteViewSet
import rest_framework
router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('/auth',include('rest_framework.urls'))
]
