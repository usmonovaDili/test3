# Generated by Django 4.2.3 on 2023-07-27 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('yozuvchi', models.CharField(max_length=40)),
                ('publish_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]