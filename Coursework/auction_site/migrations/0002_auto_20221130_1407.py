# Generated by Django 3.2.5 on 2022-11-30 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 14, 7, 34, 15648)),
        ),
        migrations.AlterField(
            model_name='products',
            name='picture',
            field=models.ImageField(default='frontend/src/images/ItemNoImage.jpg', upload_to='./frontend/src/images/ItemImages'),
        ),
        migrations.AlterField(
            model_name='replies',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 14, 7, 34, 14646)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 14, 7, 34, 14646)),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='frontend/src/images/default_user.png', upload_to='./frontend/src/images/UserImages'),
        ),
    ]
