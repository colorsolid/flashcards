# Generated by Django 4.0.3 on 2022-03-16 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_flashcard_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='cue_expanded',
            field=models.CharField(default='', max_length=100),
        ),
    ]
