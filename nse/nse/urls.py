from django.contrib import admin
from django.urls import path
from nseapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home' ),

    path('bhavcopy/',views.bhavcopy,name='bhavcopy'),
    path('gainloose/',views.gainloose,name='gainloose'),
    path('fpidata/',views.fpidata,name='fpidata'),
]
