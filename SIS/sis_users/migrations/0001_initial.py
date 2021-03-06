# Generated by Django 2.0.5 on 2018-06-04 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('class_groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='class_groups.ClassGroup')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('year', models.IntegerField(choices=[(10, 'Grade 10'), (11, 'Grade 11'), (12, 'Grade 12')], null=True)),
                ('band', models.CharField(choices=[('T', 'Technical'), ('V', 'Vocational')], max_length=1, null=True)),
                ('set', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], null=True)),
            ],
        ),
    ]
