# Generated by Django 4.1.2 on 2023-02-22 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_remove_standarddeck_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='standarddeck',
            name='avgplace',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='standarddeck',
            name='windefencerate',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='standarddeck',
            name='winrate',
            field=models.FloatField(null=True),
        ),
    ]
