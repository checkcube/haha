# Generated by Django 5.0.6 on 2024-05-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=15),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
