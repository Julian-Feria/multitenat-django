from django.urls import path
from rest_framework.routers import DefaultRouter


from productos.views import ProductosViewSet

urlpatterns = [ ]
router = DefaultRouter()

router.register(r'productos', ProductosViewSet)


urlpatterns += router.urls