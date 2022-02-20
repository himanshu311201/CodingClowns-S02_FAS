from django.urls import path
from .views import home, final

urlpatterns = [
    # path('/home/togo', togo, name='togo'),
    path('', home, name='home1'),
    path('/<po>', final, name="final")
]
