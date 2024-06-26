# Generated by Django 5.0.6 on 2024-05-24 15:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='minor1/')),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('HB', 'Hatch back'), ('Lx', 'luxury'), ('Cp', 'Coupe'), ('Ul', 'Ultra luxury')], max_length=2)),
            ],
        ),
    ]
