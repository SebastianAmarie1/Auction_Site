from django.contrib import admin
from .models import User, Products, Review, Replies, Bids

# Register your models here.
admin.site.register(User)
admin.site.register(Products)
admin.site.register(Review)
admin.site.register(Replies)
admin.site.register(Bids)