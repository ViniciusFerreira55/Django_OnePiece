# Generated by Django 4.1.1 on 2022-09-19 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0003_alter_characters_recompensa_personagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='characters',
            name='foto',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]