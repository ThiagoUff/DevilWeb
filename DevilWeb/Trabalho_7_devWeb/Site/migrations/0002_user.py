# Generated by Django 2.1.3 on 2018-11-04 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('cpf', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=20)),
                ('data_cadastro', models.DateField(null=True)),
            ],
            options={
                'db_table': 'User',
                'ordering': ('nome',),
            },
        ),
    ]
