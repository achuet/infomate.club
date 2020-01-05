# Generated by Django 2.2.8 on 2020-01-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0011_auto_20200104_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='uniq_id',
            field=models.TextField(db_index=True, default='uniq'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=2048),
        ),
    ]