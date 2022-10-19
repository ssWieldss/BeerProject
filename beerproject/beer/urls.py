from django.urls import path

from . import views
from .views import*

urlpatterns = [
    path('registration', views.SignUpView.as_view(), name='registration'),
    path('login', views.SignInView.as_view(), name='login'),
    path('main_menu', views.beer_all_view, name='main_menu'),
    path('first_beer', views.first_beer, name='first_beer'),
    path('second_beer', views.second_beer, name='second_beer'),
    path('authors', views.outro, name='authors'),
    path('', views.main_page, name='main_page'),
    path('logout', views.logout_user, name='logout'),
    path('beer/<int:pk>/', views.BeerView.as_view(), name="beer_page"),
    path('like/', views.like, name='like'),
    path('get_likes_count/<int:pk>/', views.get_likes_count, name='get_likes_count')
]