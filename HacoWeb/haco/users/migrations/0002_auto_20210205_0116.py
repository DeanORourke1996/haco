# Generated by Django 3.1.6 on 2021-02-05 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, null=True, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='user',
            name='second_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Last Name'),
        ),
    ]