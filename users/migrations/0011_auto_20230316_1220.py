# Generated by Django 3.1.14 on 2023-03-16 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200317_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Имя', models.CharField(max_length=50)),
                ('Почта', models.EmailField(max_length=254)),
                ('Номер_телефона', models.CharField(max_length=15)),
                ('Профиль', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Requests',
        ),
    ]
