from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('show/',views.show,name='show'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('news/<int:id>/',views.news_portal,name='news_portal'),

]