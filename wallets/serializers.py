from rest_framework import serializers
from .models import Operation


class OperationSerializer(serializers.Serializer):
    operation_type = serializers.ChoiceField(
        choices=Operation.OPERATION_CHOICES)
    amount = serializers.IntegerField(min_value=1)
