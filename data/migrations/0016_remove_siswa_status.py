# Generated by Django 3.1.2 on 2021-07-31 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_auto_20210731_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siswa',
            name='status',
        ),
    ]
