# Generated by Django 3.2.25 on 2024-04-19 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=85)),
                ('model', models.CharField(max_length=85)),
                ('spec', models.CharField(max_length=255)),
                ('year', models.PositiveSmallIntegerField()),
                ('fuel', models.CharField(max_length=85)),
                ('km', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=85)),
                ('fipe', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, default=None, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]