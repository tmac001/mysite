from django.urls import path
from .views import blog_detail, blog_type_list, blog_list

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('<int:blog_id>', blog_detail, name='blog_detail'),
    path('type/<int:blog_type_id>', blog_type_list, name='blog_type_list'),

]
