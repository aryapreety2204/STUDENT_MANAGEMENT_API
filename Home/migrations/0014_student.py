# Generated by Django 5.0.4 on 2024-05-10 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.IntegerField(default=0)),
                ('college', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('image', models.FileField(upload_to='student/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.courses')),
            ],
        ),
    ]
