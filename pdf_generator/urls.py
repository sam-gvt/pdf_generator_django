
from django.contrib import admin
from django.urls import path, include
from pdf import views



urlpatterns = [
    path('pdf/<int:id>/', views.cv, name='cv'),
    path('pdf/', views.accept, name='accept'),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
