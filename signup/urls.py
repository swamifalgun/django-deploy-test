from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.sign_up, name='sign_up'),
    #path('accounts/facebook/login/callback/', views.handle_callback, name='handle_callback'),
]