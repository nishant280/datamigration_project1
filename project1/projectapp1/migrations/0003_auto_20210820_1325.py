# Generated by Django 3.2.6 on 2021-08-20 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp1', '0002_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='Address Here', max_length=200),
        ),
    ]
