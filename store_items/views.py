from django.shortcuts import render
from rest_framework import views, response, permissions, status
from users import authentication
from . import serializer as store_item_serializer
from . import services


class CreateOrderAPI(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        """
        Create an order for a user.
        """
        serializer = store_item_serializer.OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        serializer.instance = services.create_order(
            user=request.user, order=data)

        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        '''
        Get all orders by user.
        '''
        print('request meta HTTP_COOKIE:', request.META.get('HTTP_COOKIE'))
        print('request meta user:', request.META.get('user'))
        print('request user:', request.user)
        user_orders = services.get_orders(request.user)

        order_list = store_item_serializer.OrderSerializer(
            user_orders, many=True)

        return response.Response(data=order_list.data, status=status.HTTP_200_OK)


class RetrieveUpdateDeleteOrdersAPI(views.APIView):
    """
    This class is used to retrieve, update or delete orders based on ID.
    """

    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, order_id):
        """
        This method retrieves the specific order details of the given id and 
        returns it in json format if found else raises 404 error code.
        """
        order_details_raw = services.get_order_details(
            request.user, order_id=order_id)

        order_list_serialized = store_item_serializer.OrderSerializer(
            order_details_raw)

        return response.Response(data=order_list_serialized.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        """
        This method updates an order using the specific order details of the given id 
        and returns it in json format if found else raises 404 error code.
        """
        serializer = store_item_serializer.OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        serializer.instance = services.update_order(
            user=request.user, order=data, order_id=order_id)

        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, order_id):
        """
        This method deletes a particular order from database by its unique
        identifier i.e., Order Id provided as parameter. If not present then
        raises HTTP Not Found Error with appropriate message.
        """
        order_delete = services.delete_order(
            user=request.user, order_id=order_id)

        return response.Response(data=order_delete, status=status.HTTP_204_NO_CONTENT)
