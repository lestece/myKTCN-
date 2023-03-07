# Generated by Django 3.2.18 on 2023-03-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.IntegerField(choices=[(0, 'STARTERS'), (1, 'MAINS'), (2, 'SIDES'), (3, 'DESSERTS'), (4, 'SNACKS')], default=0),
        ),
    ]
