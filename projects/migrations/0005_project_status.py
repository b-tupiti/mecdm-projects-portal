# Generated by Django 4.1.6 on 2023-02-13 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_statuscategory_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.status'),
        ),
    ]