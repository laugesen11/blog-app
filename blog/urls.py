from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
        path('',BlogListView.as_view(),name='home'),
        #int:pk - says the primary key 'pk' is an int
        path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
        ]
