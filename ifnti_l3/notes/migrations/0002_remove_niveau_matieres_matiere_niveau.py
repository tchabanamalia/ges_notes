# Generated by Django 4.1.2 on 2022-10-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='niveau',
            name='matieres',
        ),
        migrations.AddField(
            model_name='matiere',
            name='niveau',
            field=models.ManyToManyField(to='notes.niveau'),
        ),
    ]
