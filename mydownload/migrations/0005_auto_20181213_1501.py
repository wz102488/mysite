# Generated by Django 2.1.4 on 2018-12-13 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mydownload', '0004_auto_20181213_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wenzhang',
            name='fileLink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydownload.Files', verbose_name='文件'),
        ),
    ]
