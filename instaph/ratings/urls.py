from .views import UserViewSet, PhotoViewSet, RatingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'photos', PhotoViewSet, base_name='photo')
router.register(r'ratings', RatingViewSet, base_name='rating')


urlpatterns = router.urls