from rest_framework.generics import CreateAPIView
from .serializers import TicketSerializer


class TicketCreateAPIView(CreateAPIView):
    serializer_class = TicketSerializer
