from django.urls import path
from .views import (
    JacketListView, JacketCreateView, JacketDetailView,
    JacketUpdateView, JacketDeleteView
)

urlpatterns = [
    path('jackets/', JacketListView.as_view(), name='jacket_list'),
    path('jackets/new/', JacketCreateView.as_view(), name='jacket_create'),
    path('jackets/<int:pk>/', JacketDetailView.as_view(), name='jacket_detail'),
    path('jackets/<int:pk>/edit/', JacketUpdateView.as_view(), name='jacket_update'),
    path('jackets/<int:pk>/delete/', JacketDeleteView.as_view(), name='jacket_delete'),
]