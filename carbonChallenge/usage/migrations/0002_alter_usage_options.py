# Generated by Django 3.2.6 on 2021-08-02 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usage',
            options={'ordering': ['-usage_at'], 'verbose_name': 'Usage', 'verbose_name_plural': 'Usages'},
        ),
    ]
