# Generated by Django 5.0.4 on 2024-05-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.CharField(max_length=220)),
                ('fees', models.IntegerField()),
                ('duration', models.CharField(max_length=50)),
            ],
        ),
    ]
