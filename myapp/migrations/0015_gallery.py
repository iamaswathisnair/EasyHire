# Generated by Django 3.2.5 on 2023-12-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_workerbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workername', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=500)),
                ('imgg', models.ImageField(upload_to='')),
            ],
        ),
    ]
