# Generated by Django 4.2 on 2023-04-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_feedback', '0004_auto_20180612_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='meta',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
