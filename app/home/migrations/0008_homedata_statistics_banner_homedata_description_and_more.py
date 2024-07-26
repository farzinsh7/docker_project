# Generated by Django 5.0.6 on 2024-06-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_statistics_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='homedata',
            name='Statistics_banner',
            field=models.ImageField(null=True, upload_to='home/banner'),
        ),
        migrations.AddField(
            model_name='homedata',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='header_img',
            field=models.ImageField(null=True, upload_to='home/header'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='about_img',
            field=models.ImageField(upload_to='home/banner'),
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
