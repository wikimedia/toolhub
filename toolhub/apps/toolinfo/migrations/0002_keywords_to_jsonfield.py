# Generated by Django 2.2.17 on 2020-11-30 19:06

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('toolinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='keywords',
            field=jsonfield.fields.JSONField(blank=True, default=list, null=True),
        ),
    ]
