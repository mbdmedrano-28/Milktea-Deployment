# Generated by Django 3.2 on 2021-05-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
