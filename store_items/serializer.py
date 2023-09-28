from rest_framework import serializers
from users import serializer as user_serializer
from . import services as store_item_service


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = user_serializer.UserSerializer(read_only=True)
    item = serializers.CharField()
    quantity = serializers.IntegerField()
    notes = serializers.CharField()
    is_completed = serializers.BooleanField()
    created_date = serializers.DateTimeField(read_only=True)
    modified_date = serializers.DateTimeField(read_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return store_item_service.OrderDataClass(**data)
