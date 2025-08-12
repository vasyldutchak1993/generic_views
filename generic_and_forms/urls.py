from django.urls import path
from .views import (
    JacketListView, JacketCreateView, JacketDetailView,
    JacketUpdateView, JacketDeleteView
)

urlpatterns = [
    path('', JacketListView.as_view(), name='jacket_list'),
    path('new/', JacketCreateView.as_view(), name='jacket_create'),
    path('<int:pk>/', JacketDetailView.as_view(), name='jacket_detail'),
    path('<int:pk>/edit/', JacketUpdateView.as_view(), name='jacket_update'),
    path('<int:pk>/delete/', JacketDeleteView.as_view(), name='jacket_delete'),
]