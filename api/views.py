from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Event, Registration, User, Venue, Ticket
from .serializers import EventSerializer, RegistrationSerializer, UserSerializer, VenueSerializer, TicketSerializer

# Event ViewSet
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    # Custom action to retrieve events created by the authenticated user
    @action(detail=False, methods=['get'])
    def my_events(self, request):
        user = request.user
        events = Event.objects.filter(created_by=user)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

# Registration ViewSet
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Venue ViewSet
class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

# Ticket ViewSet
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
