# Generated by Django 4.2.5 on 2024-01-31 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsystem', '0003_remove_customuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='money',
            field=models.IntegerField(default=100),
        ),
    ]
