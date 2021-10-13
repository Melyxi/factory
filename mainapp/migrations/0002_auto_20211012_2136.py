# Generated by Django 2.2.10 on 2021-10-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='questions',
        ),
        migrations.AddField(
            model_name='survey',
            name='questions',
            field=models.ManyToManyField(blank=True, to='mainapp.Question'),
        ),
    ]
