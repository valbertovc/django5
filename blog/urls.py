from django.urls import path, include

from blog import viewsets

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', viewsets.PostViewSet)
router.register(r'comments', viewsets.CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]