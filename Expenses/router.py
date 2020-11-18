from django.urls import path
from rest_framework import routers
from Expenses import viewsets as expenseviewsets


router = routers.DefaultRouter()
router.register('', expenseviewsets.ExpensesViewSet, basename='Expenses')

urlpatterns = router.urls
