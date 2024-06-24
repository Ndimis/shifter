# Generated by Django 5.0.6 on 2024-06-21 06:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer_mgn', '0002_initial'),
        ('personnel_mgn', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_mgn.client')),
                ('créé_par', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incidents_crees', to=settings.AUTH_USER_MODEL)),
                ('lieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_mgn.maison')),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnel_mgn.personnel')),
            ],
        ),
    ]