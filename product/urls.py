from django.urls import path
from product.views import product_details_view,data

urlpatterns = [
    path('product/',product_details_view),
    path('data/',data ),
]