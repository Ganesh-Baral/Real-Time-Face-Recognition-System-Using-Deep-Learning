# Generated by Django 4.1.1 on 2022-09-29 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_attendance_section_attendance_semester_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='attendance',
            name='datentime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 0, 12, 40, 678738)),
        ),
    ]
