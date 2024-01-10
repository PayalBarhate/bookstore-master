from django.urls import path,include
from.import views


urlpatterns = [
    path('', views.index, name="index"),
    path('shop/', views.shop, name="shop"),
    path('about/', views.about, name="about"),
    path('product/<int:myid>', views.product, name="product"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact, name="contact"),
    path('search/', views.search, name='search'),
    path('bill/', views.bill, name='bill'),

]