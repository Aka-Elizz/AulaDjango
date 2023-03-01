from django.urls import path, include
from produtos.views import *

urlpatterns = [
    path('', index),
    path('produtos/', produtos)

]