# Generated by Django 4.1.7 on 2023-03-10 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20200317_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klasa',
            name='images',
            field=models.ImageField(default='cat_images/default.jpg', upload_to='cat_images'),
        ),
    ]
