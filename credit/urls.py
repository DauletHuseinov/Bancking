from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:id>/detail/', views.ClientDetailView.as_view(template_name='detail.html'), name='detail'),
]
