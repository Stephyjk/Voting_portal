# Generated by Django 3.2.4 on 2021-06-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_page', '0014_rename_position_text_position_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='body',
            field=models.TextField(verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='total_vote',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
