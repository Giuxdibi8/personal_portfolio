# Generated by Django 3.2.2 on 2021-05-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_remove_project_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(default=11112020),
            preserve_default=False,
        ),
    ]
