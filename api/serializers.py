from rest_framework import serializers
from .models import Event, Registration, User, Venue, Ticket

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']

# Event Serializer
class EventSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date_time', 'location', 'created_by', 'created_at', 'updated_at']

# Registration Serializer
class RegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Registration
        fields = ['id', 'user', 'event', 'registration_date', 'ticket_type', 'number_of_tickets', 'price_paid', 'status']

# Venue Serializer
class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ['id', 'name', 'address', 'capacity', 'contact_info', 'venue_type']

# Ticket Serializer
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'event', 'type', 'price', 'availability']
