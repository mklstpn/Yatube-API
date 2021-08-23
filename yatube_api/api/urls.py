from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'follow', FollowViewSet, basename='follow')

jwt_urls = [
    path('jwt/', include('djoser.urls')),
    path('jwt/', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(jwt_urls)),
]
