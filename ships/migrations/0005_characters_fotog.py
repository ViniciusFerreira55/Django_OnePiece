# Generated by Django 4.1.1 on 2022-09-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0004_alter_characters_akumanomi_personagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='characters',
            name='fotog',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
