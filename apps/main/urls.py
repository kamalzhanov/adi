from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MainAPIView, MainViewSet

router = DefaultRouter()
router.register(r'main-viewset', MainViewSet, basename='main-viewset')

urlpatterns = [
    path('api-view/', MainAPIView.as_view(), name='main-api-view'),
    path('', include(router.urls)),
]

from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="?",
      default_version='v1',
      description="?",
      terms_of_service="https://jut.su/",
      contact=openapi.Contact(email="kamalzhanov118@gmail.com")
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
