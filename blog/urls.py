from django.urls import path
from .views import home,login,post_detail,post,register
urlpatterns = [
    # path('order/', pizza_create, name='order'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('post_detail/', post_detail, name='post_detail'),
    path('post/', post, name='post'),
    path('register/', register, name='register'),
]
