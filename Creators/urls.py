from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.createform, name="index"),
    path('Question/<prod_id>', views.Question, name="Question"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)