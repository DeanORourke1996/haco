# Generated by Django 3.2 on 2021-07-15 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210322_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='resolution',
            field=models.CharField(default='modis', max_length=5),
            preserve_default=False,
        ),
    ]
