# Generated by Django 3.1.2 on 2021-06-27 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20210623_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokumen',
            name='npm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.siswa'),
        ),
    ]