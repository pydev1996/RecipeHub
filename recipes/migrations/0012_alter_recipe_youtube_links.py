# Generated by Django 3.2.4 on 2023-06-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_alter_recipe_youtube_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='youtube_links',
            field=models.URLField(default='https://www.youtube.com/'),
        ),
    ]
