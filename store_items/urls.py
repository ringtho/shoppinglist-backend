from django.urls import path
from . import views

urlpatterns = [
    path("orders/", views.CreateOrderAPI.as_view(), name='order'),
    path("orders/<int:order_id>",
         views.RetrieveUpdateDeleteOrdersAPI.as_view(), name='order_details')
]
