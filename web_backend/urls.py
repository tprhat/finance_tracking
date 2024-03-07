from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('add-data', views.add_data, name='add_data'),
    path('manage-budget', views.manage_budget, name='manage_budget'),
]
