# Generated by Django 3.1.1 on 2021-11-17 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0004_classification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='classification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='check.classification'),
        ),
    ]
