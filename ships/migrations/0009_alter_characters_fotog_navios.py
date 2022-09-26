# Generated by Django 4.1.1 on 2022-09-26 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0008_alter_characters_akumanomi_personagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='fotog',
            field=models.ImageField(upload_to=''),
        ),
        migrations.CreateModel(
            name='Navios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_navio', models.CharField(max_length=50)),
                ('descricao_navio', models.TextField()),
                ('foto_navio', models.ImageField(upload_to='')),
                ('nome_capitao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ships.characters')),
            ],
        ),
    ]
