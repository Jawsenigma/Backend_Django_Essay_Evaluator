# Generated by Django 4.2.5 on 2024-06-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_sso', '0003_rename_created_at_essay_date_submitted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='content_related',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
