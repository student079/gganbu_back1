# Generated by Django 4.1.2 on 2023-03-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_remove_doubledeck_h_aug_remove_doubledeck_augments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deckdata',
            name='matchid',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
