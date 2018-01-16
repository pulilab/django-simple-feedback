from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Ticket
        fields = '__all__'
