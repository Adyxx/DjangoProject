# Generated by Django 3.2 on 2021-04-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_animal_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='place',
            field=models.CharField(max_length=200, verbose_name='Latin name'),
        ),
    ]
