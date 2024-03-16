# Generated by Django 4.2.7 on 2024-01-02 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_checkoutdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoutdb',
            name='Town',
        ),
        migrations.AlterField(
            model_name='checkoutdb',
            name='Phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkoutdb',
            name='Postcode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]