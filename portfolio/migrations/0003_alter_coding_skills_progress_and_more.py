# Generated by Django 4.0 on 2021-12-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_coding_skills_design_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coding_skills',
            name='progress',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='design_skills',
            name='progress',
            field=models.IntegerField(),
        ),
    ]