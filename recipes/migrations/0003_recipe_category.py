# Generated by Django 3.2.4 on 2023-05-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20230528_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('veg', 'Vegetarian'), ('non_veg', 'Non-Vegetarian'), ('breakfast', 'Breakfast'), ('snacks', 'Snacks'), ('rice', 'Rice')], default='veg', max_length=20),
        ),
    ]
