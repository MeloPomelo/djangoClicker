# Generated by Django 4.0.4 on 2022-05-31 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_core_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='core',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
