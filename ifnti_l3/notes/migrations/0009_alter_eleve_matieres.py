# Generated by Django 4.1.2 on 2022-12-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_alter_eleve_matieres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='matieres',
            field=models.ManyToManyField(blank=True, to='notes.matiere', verbose_name='Matières'),
        ),
    ]
