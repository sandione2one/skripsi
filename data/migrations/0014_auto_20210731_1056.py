# Generated by Django 3.1.2 on 2021-07-31 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_auto_20210727_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dokumen',
            old_name='npm',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='ortu',
            old_name='npm',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='siswa',
            name='npm',
        ),
    ]
