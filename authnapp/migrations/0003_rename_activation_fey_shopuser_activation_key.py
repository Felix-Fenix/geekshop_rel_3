# Generated by Django 3.2.11 on 2022-02-18 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0002_auto_20220218_0708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopuser',
            old_name='activation_fey',
            new_name='activation_key',
        ),
    ]
