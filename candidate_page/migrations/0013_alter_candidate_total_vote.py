# Generated by Django 3.2.4 on 2021-06-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_page', '0012_rename_post_position_position_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='total_vote',
            field=models.IntegerField(default=0),
        ),
    ]
