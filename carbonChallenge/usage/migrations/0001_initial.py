# Generated by Django 3.2.5 on 2021-07-29 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsageType',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=5)),
                ('factor', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'UsageType',
                'verbose_name_plural': 'UsageTypes',
            },
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('usage_at', models.DateTimeField(null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('usage_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usage.usagetype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usage',
                'verbose_name_plural': 'Usages',
            },
        ),
    ]
