# Generated by Django 4.2.7 on 2023-11-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='colors',
            field=models.ManyToManyField(to='MainApp.color'),
        ),
    ]
