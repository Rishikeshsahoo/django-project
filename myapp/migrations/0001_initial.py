# Generated by Django 4.2.16 on 2024-10-28 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('number_of_employees', models.IntegerField(default=0)),
                ('company_address', models.CharField(max_length=255)),
                ('company_type', models.CharField(choices=[('tech', 'Tech'), ('non-tech', 'Non-Tech'), ('financial', 'Financial'), ('healthcare', 'Healthcare')], default='tech', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_duration', models.IntegerField()),
                ('start_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('number_of_member', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_email', models.CharField(max_length=100)),
                ('emp_phone_number', models.CharField(max_length=15)),
                ('emp_address', models.CharField(max_length=255)),
                ('join_date', models.DateField()),
                ('emp_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('emp_dob', models.CharField(max_length=12)),
                ('is_manager', models.BooleanField(default=True)),
                ('Company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.company')),
                ('Project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
    ]
