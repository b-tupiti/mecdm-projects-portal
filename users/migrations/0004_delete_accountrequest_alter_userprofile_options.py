# Generated by Django 4.1.6 on 2023-02-08 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_accountrequest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccountRequest',
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['-user_type', 'username']},
        ),
    ]
