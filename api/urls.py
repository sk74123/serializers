from django.urls import path, include
from .views import home, BrandList, BrandUpdate


urlpatterns = [
    path('', home),
    path('brand', BrandList.as_view()),
    path('update/<int:pk>', BrandUpdate.as_view())
]
