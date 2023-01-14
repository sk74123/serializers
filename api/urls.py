from django.urls import path, include
from .views import home, brand_list, brand_update


urlpatterns = [
    path('', home),
    path('brand', brand_list),
    path('update/<int:pk>', brand_update)
]
