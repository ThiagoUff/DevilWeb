# Generated by Django 2.1.2 on 2018-10-28 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem_desc', models.CharField(max_length=200)),
                ('imagem_src', models.CharField(max_length=200)),
            ],
        ),
    ]
