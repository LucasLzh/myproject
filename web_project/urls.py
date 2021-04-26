from django.urls import path
from .views import *

app_name = 'web'

urlpatterns = [
    path('', main_page),
    path('auto_sys.html/', auto_sys),
    path('solutions.html/', solutions),
    path('product.html/', product),
    # path('page/(\d{4})/$', page),
]