# Generated by Django 4.2 on 2023-04-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='phone',
            field=models.CharField(default=12312312345, max_length=20),
            preserve_default=False,
        ),
    ]
