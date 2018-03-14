from .views import UserViewSet, PhotoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'photos', PhotoViewSet, base_name='photo')


urlpatterns = router.urls