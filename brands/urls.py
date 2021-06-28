from django.urls import path
from .views import BootstrapFilterView
urlpatterns = [
    path('', BootstrapFilterView, name = "pretraga"),
    # path('', get_brands, name = "get_brands"),
]



