# Generated by Django 2.2.12 on 2022-12-12 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_eleve_options_alter_matiere_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='matieres',
            field=models.ManyToManyField(blank=True, editable=False, to='notes.Matiere', verbose_name='Matières'),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='prenom',
            field=models.CharField(max_length=50, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='prenom',
            field=models.CharField(max_length=50, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='niveau',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='note',
            name='valeur',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(20.0)]),
        ),
    ]
