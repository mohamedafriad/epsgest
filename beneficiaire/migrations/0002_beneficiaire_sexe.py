# Generated by Django 2.2 on 2019-11-17 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiaire',
            name='sexe',
            field=models.CharField(blank=True, choices=[('M', 'Masuclin'), ('F', 'Féminin')], max_length=20),
        ),
    ]
