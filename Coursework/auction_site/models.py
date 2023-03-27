from django.db import models
from datetime import datetime
from django.core import serializers
from django.contrib.auth.models import AbstractUser
# USE THE CUSTOM USER MODEL
''' This section defines the user database model '''


class User(AbstractUser):
    city = models.CharField(max_length=50, blank=True)
    dob = models.DateField(blank=True)
    profile_picture = models.ImageField(default="./default_user.png", null=True, blank=True)

    def __str__(self) -> str:
        return self.username

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'city': self.city,
            'dob': self.dob,
            'email': self.email,
            'password': self.password,
            'profile_picture': self.profile_picture.url,
        }


'''This Model is for the information of each product'''


class Products(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, blank=True)
    starting_price = models.IntegerField(default=0)
    picture = models.ImageField(default="./ItemNoImage.jpg", null=True, blank=True)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    sold = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'owner': self.owner.to_dict(),
            'description': self.description,
            'starting_price': self.starting_price,
            'start_date': self.start_date.strftime('%H:%M:%S    %d/%m/%y'),
            'finish_date': self.finish_date.strftime('%H:%M:%S    %d/%m/%y'),
            'picture': self.picture.url,
            'sold': self.sold,
        }


'''This model is for leaving a question on a product'''


class Review(models.Model):
    message = models.CharField(max_length=255)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.message

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'message': self.message,
            'sender': self.sender.to_dict(),
            'item': self.item.to_dict(),
            'date_posted': self.date_posted.strftime('%H:%M:%S    %d/%m/%y'),
        }


'''The Model is for the replies for any review that is left on the product.'''


class Replies(models.Model):
    replying = models.ForeignKey(Review, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.message

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'replying': self.replying.to_dict(),
            'message': self.message,
            'sender': self.sender.to_dict(),
            'item': self.item.to_dict(),
            'date_posted': self.date_posted.strftime('%H:%M:%S    %d/%m/%y'),
        }


'''Model that stores all the bids for each item'''


class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return str(self.amount)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'user': self.user.to_dict(),
            'product': self.product.to_dict(),
            'amount': self.amount,
            'date_posted': self.date_posted,
        }
