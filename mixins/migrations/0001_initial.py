# Generated by Django 4.2.3 on 2023-08-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=50)),
            ],
        ),
    ]
