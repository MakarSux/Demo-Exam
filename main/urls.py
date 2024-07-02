from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('create_statement/', create_statement, name='create_statement'),
    path('about/', about, name="about"),
     path('<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)