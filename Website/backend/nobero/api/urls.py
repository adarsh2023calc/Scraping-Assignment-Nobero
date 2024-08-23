
from  django.urls import path,include

from .views import ProductView
from rest_framework.routers import DefaultRouter
from .views import ProductView


router = DefaultRouter()
router.register(r'products',ProductView,basename='product')


urlpatterns=[
    
   path('api/products/', ProductView.get_products, name='product-list'),
    path('api/', include(router.urls))
]

