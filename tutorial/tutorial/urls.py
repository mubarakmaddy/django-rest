from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from quickstart import views

router = routers.DefaultRouter()
router.register(r'user-view-set', views.UserViewSet)
router.register(r'group-view-set', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('users/', views.Users.as_view()),
    path('groups/', views.Groups.as_view()),
]
