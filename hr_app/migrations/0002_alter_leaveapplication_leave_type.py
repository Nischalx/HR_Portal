# Generated by Django 5.1.7 on 2025-03-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='leave_type',
            field=models.CharField(choices=[('Sick Leave', 'Sick Leave'), ('Casual Leave', 'Casual Leave'), ('Paid Leave', 'Paid Leave'), ('Unpaid Leave', 'Unpaid Leave')], max_length=50),
        ),
    ]
