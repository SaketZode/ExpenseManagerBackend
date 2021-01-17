from rest_framework import routers

from Friendlist.viewsets import FriendlistViewSet

router = routers.DefaultRouter()
router.register('', viewset=FriendlistViewSet)

urlpatterns = router.urls
