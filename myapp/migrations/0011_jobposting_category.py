# Generated by Django 3.2.5 on 2023-12-01 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_dailyweges_jobposting_dailywages'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='category',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]