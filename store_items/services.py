import dataclasses
import datetime
from typing import TYPE_CHECKING
from users import services as user_services
from users.models import User
from . import models as order_models
from django.shortcuts import get_object_or_404
from rest_framework import status, exceptions

if TYPE_CHECKING:
    from .models import Order


@dataclasses.dataclass
class OrderDataClass:
    """
    Order Data Class for creating orders and updating them
    """
    item: str
    quantity: int
    notes: str
    is_completed: bool = None
    id: int = None
    user: user_services.UserDataClass = None
    created_date: datetime.date = None
    modified_date: datetime.date = None

    @classmethod
    def from_instance(cls, order_model: 'Order') -> "OrderDataClass":
        return cls(
            id=order_model.id,
            user=order_model.user,
            item=order_model.item,
            quantity=order_model.quantity,
            is_completed=order_model.is_completed,
            notes=order_model.notes,
            created_date=order_model.created_date,
            modified_date=order_model.modified_date,
        )


"""
Functions to handle CRUD operations
"""


def create_order(user, order: "OrderDataClass") -> "OrderDataClass":
    new_order = order_models.Order.objects.create(
        user=user,
        item=order.item,
        quantity=order.quantity,
        notes=order.notes,
        is_completed=order.is_completed
    )

    new_order.save()

    return OrderDataClass.from_instance(order_model=new_order)


def get_orders(user) -> list["OrderDataClass"]:
    filtered_orders = order_models.Order.objects.filter(user=user)

    orders_list = [OrderDataClass.from_instance(
        order_model=order) for order in filtered_orders]

    return orders_list


def get_order_details(order_id: int) -> "OrderDataClass":
    """
    Get a single order by ID and returns it as an object with all the details of that particular order
    """
    order_detail = get_object_or_404(order_models.Order, pk=order_id)

    return OrderDataClass.from_instance(order_detail)


def update_order(user: "User", order: "OrderDataClass", order_id: int) -> "OrderDataClass":
    retrieved_order = get_object_or_404(order_models.Order, pk=order_id)

    if (retrieved_order.user.id != user.id):
        raise exceptions.PermissionDenied("Access denied!")

    retrieved_order.item = order.item
    retrieved_order.quantity = order.quantity
    retrieved_order.notes = order.notes
    retrieved_order.is_completed = order.is_completed

    retrieved_order.save()

    return OrderDataClass.from_instance(order_model=retrieved_order)


def delete_order(user: "User", order_id: int):
    order = get_object_or_404(order_models.Order, pk=order_id)

    if (order.user.id != user.id):
        raise exceptions.PermissionDenied("Access denied!")

    order.delete()
