"""ExpenseManagerBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from Expenses import router as expensesrouter
from Lendings import router as lendingsrouter
from Borrowings import router as borrowingsrouter
from Friendlist import router as friendlistrouter
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='SwaggerUI')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('expenses/', include(expensesrouter.urlpatterns)),
    path('lendings/', include(lendingsrouter.urlpatterns)),
    path('borrowings/', include(borrowingsrouter.urlpatterns)),
    path('friendlist/', include(friendlistrouter.urlpatterns)),
    path('swagger-ui/', TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ), name='swagger-ui'),
]
