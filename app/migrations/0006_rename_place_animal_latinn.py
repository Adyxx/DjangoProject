# Generated by Django 3.2 on 2021-04-12 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_animal_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='place',
            new_name='latinn',
        ),
    ]
