# Generated by Django 2.0.5 on 2018-05-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice_board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]