# Generated by Django 3.2.5 on 2021-08-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210806_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='intro',
            field=models.TextField(blank=True, default=''),
        ),
    ]
