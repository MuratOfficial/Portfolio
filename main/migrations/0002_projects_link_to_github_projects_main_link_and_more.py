# Generated by Django 4.2.2 on 2023-06-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='link_to_github',
            field=models.CharField(default='https://github.com', max_length=128),
        ),
        migrations.AddField(
            model_name='projects',
            name='main_link',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='projects',
            name='stack1',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='projects',
            name='stack2',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='projects',
            name='stack3',
            field=models.CharField(default='', max_length=64),
        ),
    ]
