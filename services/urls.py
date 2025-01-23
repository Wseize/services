from django.urls import path
from .views import (
    CategoryDetail,
    CategoryList,
    GalleryDetail,
    GalleryList,
    ItemDetail,
    ItemList,
    NoticePersonDetailView,
    NoticePersonListCreateView,
    OrderCourierCreate,
    OrderCourierDetail,
    OrderCourierStatusUpdate,
    OrderCreate,
    OrderDetail,
    OrderStatusUpdate,
    PersonDetail,
    PersonItemViewSet,
    PersonList,
    PublicityDetail,
    PublicityList,
    RatingPersonDetailView,
    RatingPersonListCreateView,
)

urlpatterns = [

    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),

    path('galleries/', GalleryList.as_view(), name='gallery-list'),
    path('galleries/<int:pk>/',  GalleryDetail.as_view(), name='gallery-detail'),


    path('persons/', PersonList.as_view(), name='person-list'),
    path('persons/<int:pk>/', PersonDetail.as_view(), name='person-detail'),

    path('items/', ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),

    path('item-person/', PersonItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='personitem-list'),
    path('item-person/<int:pk>/', PersonItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='personitem-detail'),

    path('publicities/', PublicityList.as_view(), name='publicity-list'),
    path('publicities/<int:pk>/', PublicityDetail.as_view(), name='publicity-detail'),

    path('ratingsPerson/', RatingPersonListCreateView.as_view(), name='rating-person-list-create'),
    path('ratingsPerson/<int:pk>/', RatingPersonDetailView.as_view(), name='rating-person-detail'),

    path('notices/', NoticePersonListCreateView.as_view(), name='notice-list-create'),
    path('notices/<int:pk>/', NoticePersonDetailView.as_view(), name='notice-detail'),


    path('orders/', OrderCreate.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='service-detail'),
    path('orders/<int:pk>/status/', OrderStatusUpdate.as_view(), name='order-status-update'),

    path('ordersCourier/', OrderCourierCreate.as_view(), name='order-create'),
    path('ordersCourier/<int:pk>/', OrderCourierDetail.as_view(), name='service-detail'),
    path('ordersCourier/<int:pk>/status/', OrderCourierStatusUpdate.as_view(), name='order-status-update'),
]
