from django.urls import path, include

from AdminControlSerializers.views import UserViewSet, ProfileViewSet, PostViewSet, CommentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'post', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'user', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
print(router.urls)