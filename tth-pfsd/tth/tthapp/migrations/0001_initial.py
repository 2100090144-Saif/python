# Generated by Django 4.1.7 on 2023-03-07 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datetime1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time12', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'datetime1',
            },
        ),
    ]
