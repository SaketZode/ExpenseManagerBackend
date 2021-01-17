from rest_framework import routers
from Borrowings.viewsets import BorrowingsViewSet

router = routers.DefaultRouter()
router.register('', viewset=BorrowingsViewSet, basename='Borrowings')

urlpatterns = router.urls