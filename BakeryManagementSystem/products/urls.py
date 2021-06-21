from django.urls import path
from views import ProductViewAll

urlpatterns = [
    path('/',ProductViewAll),
]
