# Generated by Django 5.1.7 on 2025-06-02 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0026_exitrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_days', models.FloatField(default=0)),
                ('approved_by', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave'), ('H', 'Holiday')], default='P', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_app.addemployee')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('employee', 'date')},
            },
        ),
    ]
