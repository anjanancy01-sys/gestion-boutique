from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from boutique.views import CategorieViewSet, ProduitViewSet, ClientViewSet, VenteViewSet

router = DefaultRouter()
router.register(r'categories', CategorieViewSet)
router.register(r'produits', ProduitViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'ventes', VenteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]