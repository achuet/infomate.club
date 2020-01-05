# Generated by Django 2.2.8 on 2020-01-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0008_boardfeed_icon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boardfeed',
            options={'ordering': ['index']},
        ),
        migrations.AddField(
            model_name='board',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='boardfeed',
            name='last_article_at',
            field=models.DateTimeField(null=True),
        ),
    ]