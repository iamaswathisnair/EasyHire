# Generated by Django 3.2.5 on 2023-12-03 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_jobposting_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='workerreg1',
            name='imgg',
            field=models.ImageField(default=1, upload_to='worker/'),
            preserve_default=False,
        ),
    ]
