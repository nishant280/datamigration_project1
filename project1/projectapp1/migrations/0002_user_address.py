# Generated by Django 3.2.6 on 2021-08-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]