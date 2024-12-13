from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=50, choices=(('attendee', 'Attendee'), ('organizer', 'Organizer')), default='attendee')

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    max_attendees = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=(('upcoming', 'Upcoming'), ('completed', 'Completed'), ('canceled', 'Canceled')), default='upcoming')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Registration Model
class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registrations")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    registration_date = models.DateTimeField(auto_now_add=True)
    ticket_type = models.CharField(max_length=50, choices=(('regular', 'Regular'), ('vip', 'VIP')))
    number_of_tickets = models.PositiveIntegerField()
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=(('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')), default='pending')

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, choices=(('reminder', 'Reminder'), ('update', 'Update')))

# Payment Model
class Payment(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE, related_name="payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=(('success', 'Success'), ('failed', 'Failed')))
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=(('card', 'Card'), ('wallet', 'Wallet')))
    transaction_id = models.CharField(max_length=255, null=True, blank=True)

# Venue Model
class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    capacity = models.PositiveIntegerField()
    contact_info = models.TextField()
    venue_type = models.CharField(max_length=50, choices=(('indoor', 'Indoor'), ('outdoor', 'Outdoor')))

# Ticket Model
class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tickets")
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.PositiveIntegerField()

# Review Model
class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    moderated = models.BooleanField(default=False)

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

# EventCategory Model
class EventCategory(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="categories")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="events")
