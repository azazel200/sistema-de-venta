# Generated by Django 3.0.6 on 2021-01-20 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='img',
            new_name='image',
        ),
    ]
