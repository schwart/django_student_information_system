# Generated by Django 2.0.5 on 2018-06-10 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis_users', '0004_remove_staff_classes'),
        ('class_groups', '0002_auto_20180604_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('T', 'Technical'), ('V', 'Vocational')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='class_groups.Band')),
                ('subjects', models.ManyToManyField(to='class_groups.Subject')),
                ('teachers', models.ManyToManyField(to='sis_users.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(10, 'Grade 10'), (11, 'Grade 11'), (12, 'Grade 12')])),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='class_groups.School')),
            ],
        ),
        migrations.AddField(
            model_name='band',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='class_groups.Year'),
        ),
    ]
