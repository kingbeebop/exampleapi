# Generated by Django 4.2 on 2023-04-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_rename_email_lead_from_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='from_source',
            field=models.CharField(default='Answering Legal', max_length=50),
        ),
    ]
