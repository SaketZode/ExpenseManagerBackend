from rest_framework import routers
from Lendings.viewsets import LendingsViewSet


router = routers.DefaultRouter()

router.register('', viewset=LendingsViewSet, basename='Lendings')

urlpatterns = router.urls
