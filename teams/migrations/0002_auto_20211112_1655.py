# Generated by Django 3.1.12 on 2021-11-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='display_name',
            field=models.CharField(default='WEH', max_length=100),
            preserve_default=False,
        ),
    ]