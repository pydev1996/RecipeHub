# Generated by Django 3.2.4 on 2023-05-28 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='audio_description',
            new_name='audio',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_ingredients',
            new_name='ingredients',
        ),
    ]
