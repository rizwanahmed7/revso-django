# Generated by Django 4.2 on 2023-04-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='content',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
