# Generated by Django 3.2.3 on 2021-07-06 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20210705_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_number',
        ),
    ]