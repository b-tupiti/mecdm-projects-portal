# Generated by Django 4.1.6 on 2023-02-10 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projecttype_risk_project_rate_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
