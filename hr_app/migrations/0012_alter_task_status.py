# Generated by Django 5.1.7 on 2025-05-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0011_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Claimed Completed', 'Claimed Completed')], default='Pending', max_length=20),
        ),
    ]
