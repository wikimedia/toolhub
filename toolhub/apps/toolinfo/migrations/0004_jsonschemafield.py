# Generated by Django 2.2.17 on 2021-01-25 23:19

from django.db import migrations, models
import toolhub.fields


class Migration(migrations.Migration):

    dependencies = [
        ('toolinfo', '0003_track_tool_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='available_ui_languages',
            field=toolhub.fields.JSONSchemaField(blank=True, default=list, help_text="The language(s) the tool's interface has been translated into. Use ISO 639 language codes like `zh` and `scn`. If not defined it is assumed the tool is only available in English.", null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='developer_docs_url',
            field=toolhub.fields.JSONSchemaField(blank=True, default=list, help_text="A link to the tool's developer documentation, if available.", null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='feedback_url',
            field=toolhub.fields.JSONSchemaField(blank=True, default=list, help_text="A link to location where the tool's user can leave feedback.", null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='for_wikis',
            field=toolhub.fields.JSONSchemaField(blank=True, default=list, help_text="A string or array of strings describing the wiki(s) this tool can be used on. Use hostnames such as `zh.wiktionary.org`. Use asterisks as wildcards. For example, `*.wikisource.org` means 'this tool works on all Wikisource wikis.' `*` means 'this works on all wikis, including Wikimedia wikis.'", null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='keywords',
            field=toolhub.fields.JSONSchemaField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.SlugField(allow_unicode=True, help_text='Unique identifier for this tool. Must be unique for every tool. It is recommended you prefix your tool names to reduce the risk of clashes.', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='privacy_policy_url',
            field=toolhub.fields.JSONSchemaField(blank=True, default=list, help_text="A link to the tool's privacy policy, if available.", null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='sponsor',
            field=toolhub.fields.JSONSchemaField(blank=True, default=list, help_text="Organization(s) that sponsored the tool's development.", null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='technology_used',
            field=toolhub.fields.JSONSchemaField(blank=True, default=list, help_text='A string or array of strings listing technologies (programming languages, development frameworks, etc.) used in creating the tool.', null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='url_alternates',
            field=toolhub.fields.JSONSchemaField(blank=True, default=list, help_text='Alternate links to the tool or install documentation in different natural languages.', null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='user_docs_url',
            field=toolhub.fields.JSONSchemaField(blank=True, default=list, help_text="A link to the tool's user documentation, if available.", null=True),
        ),
    ]