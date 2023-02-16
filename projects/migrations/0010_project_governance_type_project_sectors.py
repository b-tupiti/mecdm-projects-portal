# Generated by Django 4.1.6 on 2023-02-16 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('govsect', '0001_initial'),
        ('projects', '0009_location_scope_project_locations_project_scope'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='governance_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='govsect.governancetype', verbose_name='Government or Non-government'),
        ),
        migrations.AddField(
            model_name='project',
            name='sectors',
            field=models.ManyToManyField(to='govsect.sector'),
        ),
    ]
