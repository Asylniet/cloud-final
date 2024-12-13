from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(Notification)
admin.site.register(Payment)
admin.site.register(Venue)
admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(EventCategory)
