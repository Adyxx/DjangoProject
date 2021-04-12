# Generated by Django 3.2 on 2021-04-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter an animal type (e.g. mammal, bird)', max_length=40, unique=True, verbose_name='Animal type')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Types',
        ),
    ]
