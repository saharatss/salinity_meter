# Generated by Django 3.1.5 on 2021-03-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210326_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='site_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
