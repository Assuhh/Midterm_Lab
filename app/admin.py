from django.contrib import admin
from .models import User, Subject, Session, Payment, Review, Appointment

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Session)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Appointment)