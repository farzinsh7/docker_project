# Generated by Django 5.0.6 on 2024-06-13 05:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('logo', models.ImageField(null=True, upload_to='logo')),
                ('mission', models.TextField(null=True)),
                ('vision', models.TextField(null=True)),
                ('value', models.TextField(null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HelpfulLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('main_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='links', to='home.siteinformation')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=120, null=True)),
                ('icon', models.CharField(max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('main_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='socials', to='home.siteinformation')),
            ],
        ),
    ]
