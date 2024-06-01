# Generated by Django 5.0.6 on 2024-05-27 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_nickname_alter_customuser_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
