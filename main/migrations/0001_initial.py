# Generated by Django 4.2.5 on 2023-09-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
                ('base_atk', models.IntegerField()),
                ('base_hp', models.IntegerField()),
                ('base_def', models.IntegerField()),
                ('rarity', models.IntegerField()),
            ],
        ),
    ]