# Generated by Django 5.0.6 on 2024-06-08 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='slider')),
                ('home_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sliders', to='brands.brands')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=120, null=True)),
                ('icon', models.CharField(max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('main_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='socials', to='brands.brands')),
            ],
        ),
    ]
