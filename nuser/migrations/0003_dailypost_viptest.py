# Generated by Django 4.0.2 on 2022-03-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuser', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='dailypost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=10000000000000000000000000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='viptest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=10000000000000000000000000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
