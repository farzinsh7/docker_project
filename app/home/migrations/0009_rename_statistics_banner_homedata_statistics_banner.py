# Generated by Django 5.0.6 on 2024-06-16 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homedata_statistics_banner_homedata_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homedata',
            old_name='Statistics_banner',
            new_name='statistics_banner',
        ),
    ]
