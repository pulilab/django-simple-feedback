from rest_framework.generics import CreateAPIView

from .serializers import TicketSerializer


class TicketCreateAPIView(CreateAPIView):
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        # TODO make this a separate package
        # TODO send email to superusers on tickets
        request.data['user'] = request.user.id if request.user.is_authenticated() else None
        return super().create(request, *args, **kwargs)
