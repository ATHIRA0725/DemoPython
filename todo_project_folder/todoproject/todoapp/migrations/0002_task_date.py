# Generated by Django 4.1.6 on 2023-02-13 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2023-02-13'),
            preserve_default=False,
        ),
    ]
