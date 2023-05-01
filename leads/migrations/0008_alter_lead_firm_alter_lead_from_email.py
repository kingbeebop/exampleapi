# Generated by Django 4.2 on 2023-05-01 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_alter_lead_from_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='firm',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='leads.firm'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='from_email',
            field=models.EmailField(max_length=200),
        ),
    ]