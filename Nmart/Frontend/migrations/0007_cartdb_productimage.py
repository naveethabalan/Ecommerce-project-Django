# Generated by Django 4.2.7 on 2024-01-03 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0006_checkoutdb_town'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='ProductImage',
            field=models.ImageField(blank=True, null=True, upload_to='Images'),
        ),
    ]
