# Generated by Django 2.2.17 on 2021-01-13 20:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolinfo', '0002_keywords_to_jsonfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='origin',
            field=models.CharField(choices=[('crawler', 'crawler'), ('api', 'api')], default='crawler', help_text='Origin of this tool record.', max_length=32),
        ),
        migrations.AlterField(
            model_name='tool',
            name='_language',
            field=models.CharField(blank=True, help_text='The language in which this toolinfo record is written. If not set, the default value is English. Use ISO 639 language codes.', max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^(x-.*|[A-Za-z]{2,3}(-.*)?)$')]),
        ),
    ]
